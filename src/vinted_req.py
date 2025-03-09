from vinted_scraper import VintedScraper

def fetch(brand_id, size_id, color_id):
    scraper = VintedScraper("https://www.vinted.co.uk")
    params = {
        "order": "newest_first",
        "brand_ids": brand_id,
        "size_ids": size_id,
        "color_ids": color_id
    }
    items = scraper.search(params)
    item = items[0]
    
    cleaned_item = {
        "title": item.title,
        "url": item.url,
        "photo": item.photo.url if item.photo else None,
        "price": item.price,
        "size": item.size_title,
        "brand": item.brand.title,
        "condition": item.status,
        "user": item.user.profile_url,
        "user-id": item.user.id,
    }
    
    return cleaned_item