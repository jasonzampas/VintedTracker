import vinted_req as vinted_req
import json
import time

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def fetch(brand):
    brand_data = load_json('data/brands.json')
    brand_id = brand_data.get(brand) 

    if not brand_id:
        raise ValueError(f"Brand '{brand}' not found in brands.json")
    
    return vinted_req.fetch(brand_id, None, None)