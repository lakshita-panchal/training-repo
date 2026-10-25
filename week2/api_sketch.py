store_inventory = {
    "1": {"name": "Health Potion", "price": 50, "stock": 12},
    "2": {"name": "Iron Sword", "price": 150, "stock": 3},
    "3": {"name": "Shield", "price": 100, "stock": 5}
}

def get_all_items_endpoint():
    print("\n[GET] /items")
    return 200, store_inventory

def get_item_by_id_endpoint(item_id):
    print(f"\n[GET] /items/{item_id}")
    if item_id in store_inventory:
        return 200, store_inventory[item_id]
    return 404, {"error": "Item not found"}

status, payload = get_all_items_endpoint()
print(f"Status: {status}\nPayload: {payload}")

status, payload = get_item_by_id_endpoint("2")
print(f"Status: {status}\nPayload: {payload}")

status, payload = get_item_by_id_endpoint("99")
print(f"Status: {status}\nPayload: {payload}")

