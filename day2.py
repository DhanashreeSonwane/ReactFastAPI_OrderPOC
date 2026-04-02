class Order:
    def __init__(self, id, item, price, status):
        self.id = id
        self.item = item
        self.price = price
        self.status = status

order1 =Order(1, "Laptop", 50000, "pending")
order2 = Order(2, "Phone", 20000, "shipped")
orders = [order1, order2]

for order in orders:
  print(order.item, order.price, order.status)

new_order = Order(3, "Tablet", 15000, "pending")
orders.append(new_order)

for order in orders:
 print(order.item, order.price, order.status)