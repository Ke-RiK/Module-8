# Kirill Kaminskyi M8P4.py 10/12/2026

#input
file = open("M8P4", "r")

total_extended_price  = 0
order_count = 0

#process + output
print(f"{"Item:":<20} {"Quantity:":<20} {"Price:":<20} {"Extended price:":<20}")

for x in range(4):
    item_name = file.readline().strip()
    item_amount = int(file.readline())
    item_price = float(file.readline())
    empty_line = file.readline()

    extended_price = item_amount * item_price
    total_extended_price += extended_price

    order_count = order_count + 1

    print(f"{item_name:<20} {item_amount:<20} ${item_price:<20,.2f} ${extended_price:<20,.2f}")

average_order = total_extended_price/ order_count

#final output
print()
print(f"Total extended price: ${total_extended_price:,.2f}")
print()
print(f"Number of orders: {order_count}")
print()
print(f"Average Order Price: ${average_order:,.2f}")