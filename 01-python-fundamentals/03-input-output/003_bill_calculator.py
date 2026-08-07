# Program: Bill Calculator

# Description: Calculates the total cost of items based on price and quantity.

item_name = input("Enter item name: ")
price = float(input("Enter price per item: Rs."))
quantity = int(input("Enter quantity: "))

total = price * quantity

print()
print("=============================")
print("            BILL")
print("=============================")
print("Item       :", item_name)
print("Price      : Rs.", price)
print("Quantity   :", quantity)
print("-----------------------------")
print("Total      : Rs.", total)
print("=============================")
print("Thank you! Visit Again.")