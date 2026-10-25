inventory = ["laptop", "mouse", "keyboard", "monitor"]
item_details = {
    "laptop": {"price": 45000, "stock": 10},
    "mouse": {"price": 800, "stock": 50},
    "keyboard": {"price": 1500, "stock": 35},
    "monitor": {"price": 12000, "stock": 12},
}
print("--- Current Store Inventory ---")
for item in inventory:
    details = item_details.get(item)

    if details:
        print(f"Item: {item.capitalize()}")
        print(f"  Price: ₹{details['price']}")
        print(f"  Stock: {details['stock']} units")
        print("-" * 30)
