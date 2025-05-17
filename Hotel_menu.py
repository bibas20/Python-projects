# Define the menu of restaurant
menu = {
    'pizza': 350,
    'Black Tea': 30,
    'Momo': 100,
    'American Chopsey': 120,
    'Coffe(milk)': 80,
    'coffe(black)': 60,
    'Salad': 120,
}

# Greet
print("Welcome to Bibas Restaurant")
print(" pizza: 350\n Black Tea: 30\n Momo: 100\n Burgure: 120\n Coffe(milk): 80\n coffe(black): 60\n Salad: 120\n")

order_totel = 0

item_1 = input("Enter the name of item you want to order: ")
if item_1 in menu:
    order_totel += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet, Thank You!")

another_order = input("Do you want to add another item? (Yes/No): ")
if another_order.lower() == "yes":
    item_2 = input("Enter the name of the second item: ")
    if item_2 in menu:
        order_totel += menu[item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available yet, Thank You!")

print(f"The total amount of items to pay is {order_totel}")