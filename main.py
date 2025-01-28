import discord
from discord.ext import commands, tasks
from discord.ui import Button, View
from discord import app_commands
import fetch
import json
import asyncio

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())
last_product_urls = {}

with open("data/brands.json", "r") as file:
    brands = list(json.load(file).keys())

with open("data/channels.json", "r") as file:
    channels = json.load(file)

def create_embed(product):
    embed = discord.Embed(title=product["title"], color=discord.Color.pink())

    embed.add_field(name="🏷️ Brand", value=product["brand"], inline=True)
    embed.add_field(name="💰 Price", value=f"£{product['price']}", inline=True)
    embed.add_field(name="👕 Size", value=product["size"], inline=True)
    embed.add_field(name="✨ Condition", value=product["condition"], inline=True)
    embed.set_image(url=product["photo"])

    return embed

def create_product_view(product):
    view = View()

    view.add_item(Button(label="View Product", url=product["url"]))
    view.add_item(Button(label="Message Seller", url=f"https://www.vinted.co.uk/inbox/new?receiver_id={product['user-id']}"))

    return view

async def send(product_name, channel_id):
    try:
        with open("data/criteria.json", "r", encoding="utf-8") as file:
            criteria = json.load(file)

        if (product_name, channel_id) not in last_product_urls:
            last_product_urls[(product_name, channel_id)] = None

        product = fetch.fetch(product_name)

        if not product:
            print(f"No product data returned for {product_name}.")
            return

        channel = bot.get_channel(channel_id)

        if channel:
            if product["price"] <= criteria["max-price"] and product["size"] in criteria["sizes"]:
                if product["url"] != last_product_urls[(product_name, channel_id)]:
                    embed = create_embed(product)
                    view = create_product_view(product)
                    last_product_urls[(product_name, channel_id)] = product["url"]

                    print(f"Sending notification for {product_name} to channel {channel_id}")
                    await channel.send(embed=embed, view=view)

    except Exception as e:
        print(f"Error in send function for {product_name}: {e}")

@tasks.loop(seconds=15)
async def snipe():
    for item in brands:
        await send(item, channels[item])

@bot.event
async def on_ready():
    print("Bot is ready!")
    try:
        await bot.tree.sync()
        print("Slash commands synced successfully!")
    except Exception as e:
        print(f"Error syncing commands: {e}")
    snipe.start()

@bot.tree.command(name="criteria", description="Update the maximum price criteria")
@app_commands.describe(price="The maximum price to filter products by (e.g., 50).")
async def criteria(interaction: discord.Interaction, price: float):
    try:
        with open("data/criteria.json", "r") as file:
            data = json.load(file)

        data["max-price"] = price

        with open("data/criteria.json", "w") as file:
            json.dump(data, file)

        await interaction.response.send_message(f"Max price updated to £{price:.2f}", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"Error updating criteria: {e}", ephemeral=True)

async def start():
    with open("token.txt", "r") as file:
        token = file

    await bot.start(token)

if __name__ == "__main__":
    import sys
    if sys.platform.startswith("win") and hasattr(asyncio, "WindowsSelectorEventLoopPolicy"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    loop = asyncio.get_event_loop()
    loop.create_task(start())
    loop.run_forever()