# VintedTracker
A simple Vinted monitor that fetches listings matching your criteria. Customize filters such as price range and brand to find the best deals for reselling.

# 👨‍💻 Set up
### Install the required dependencies
```
pip install -r requirements.txt
```

### Create a discord bot
1. Go to [https://discord.com/developers/applications/](https://discord.com/developers/applications/)

2. Press `New Application` and create an application.

3. Enable all `Privileged Gateway Intents` in the `Bot` section.

4. Invite the bot to your server with the link: [https://discord.com/api/oauth2/authorize?client_id=[YOUR BOT'S ID]&permissions=8&scope=bot%20applications.commands]()

5. In `Bot`, press `Reset Token` to retrieve your bot's token

### Make a `token.txt` file
After you cloned this repository, make a file called `token.txt` and paste the token you retrieved from the last step to this file.


# 🤖 Bot Set up

This bot fetches products from Vinted based on popular brand IDs and sends them to specific Discord channels. Follow the steps below to configure it properly.

### 📁 Files Overview
- **`data/brands.json`**: Contains Vinted brand IDs for popular brands.
- **`data/channels.json`**: Maps brand names (or IDs) to specific Discord channel IDs. This tells the bot where to send product embeds.

### 🔧 Setup Steps

### 1. Create Channels on Discord
1. Open your Discord server.
2. Decide how to organize the channels and create them:
   - **One channel per brand** (e.g., `#polo-ralph-lauren`, `#supreme`).
   - **One general channel** for all brands (e.g., `#all-products`).

### 2. Enable Developer Mode
To get the IDs of the channels:
1. Open **User Settings** in Discord.
2. Navigate to **Advanced**.
3. Toggle on **Developer Mode**.

---

### 3. Get Channel IDs
1. Right-click on each channel you created.
2. Select **Copy ID**. This gives you the unique ID for that channel.

---

### 4. Update `data/channels.json`
1. Open the file `data/channels.json`.
2. The file should look like this:
   ```json
   {
       "brand_name": 1234567890,
       "another_brand_name": 0987654321
   }

# 📃 License:

This project is licensed under the MIT License.
