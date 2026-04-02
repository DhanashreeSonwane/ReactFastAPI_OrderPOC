# Step 1: Create orders list
orders = [
    {"id": 1, "item": "Laptop", "price": 50000, "status": "pending"},
    {"id": 2, "item": "Phone", "price": 20000, "status": "shipped"}
]

# Step 2: Print all orders
print("All Orders:")
print(orders)

# Step 3: Add new order
new_order = {"id": 3, "item": "Tablet", "price": 15000, "status": "pending"}
orders.append(new_order)

print("\nAfter Adding New Order:")
print(orders)

# Step 4: Print only item names
print("\nOrder Items:")
for order in orders:
    print(order["item"])

# Step 5: Filter expensive orders
print("\nExpensive Orders (>20000):")
for order in orders:
    if order["price"] > 20000:
        print(order)

# Step 6: Function (IMPORTANT)
def get_orders():
    return orders

#to show only order having status pending
def get_pending_orders():
    pending_orders = []
    for order in orders:
        if order["status"] == "pending":
            pending_orders.append(order)
    return pending_orders

print("\nUsing Function:")
print(get_orders())
print("\nPending Orders:")
print(get_pending_orders())