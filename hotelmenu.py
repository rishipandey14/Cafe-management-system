from prettytable import PrettyTable

Dishes_list = {
    'pizza':200,
    'pasta':100,
    'burger':50,
    'chowmean':40,
    'aaloo tikki':40,
    'pakodi':30,
    'aaloo chop':50,
    'spring roll':40,
}

# Greet
print("\n Welcome to RR (Rishi Restaurant)\n")

# Define the menu of restaurant
# These 3 are the columns of the tables
menu = PrettyTable(['Sr.no', 'Dish', 'Price'])
 
# To insert rows:
menu.add_row(['1', 'pizza', 200])
menu.add_row(['2', 'pasta', 100])
menu.add_row(['3', 'burger', 50])
menu.add_row(['4', 'chowmean', 40])
menu.add_row(['5', 'aaloo tikki', 40])
menu.add_row(['6', 'pakodi', 30])
menu.add_row(['7', 'aaloo chop', 50])
menu.add_row(['8', 'spring roll', 40])
 
print(menu)

order_total = 0
ordered_items = []

# Function to display the current order summary
def display_order():
    if ordered_items:
        order_summary = PrettyTable(['Dish', 'Price'])
        for item in ordered_items:
            order_summary.add_row([item, Dishes_list[item]])
        print("\nCurrent Order:")
        print(order_summary)
    else:
        print("\nNo items in the order yet.")

# Loop to take orders
while True:
    item = input("\nWhat would you like to order (or type 'done' to finish): ").strip()
    if item.lower() == 'done':
        break
    elif item in Dishes_list:
        ordered_items.append(item)
        order_total += Dishes_list[item]
        print(f"Your item {item} has been added to your order")
    else:
        print(f"Ordered item {item} is not available yet!")
    
    display_order()
    print(f"Total Amount so far: {order_total}")

    another_action = input("\nDo you want to add more items or remove any item from your order? (Yes/No): ").strip()
    if another_action.lower() == 'no':
        break
    elif another_action.lower() == 'yes':
        action = input("Enter 'add' to add more items or 'remove' to remove an item: ").strip().lower()
        if action == 'remove':
            item_to_remove = input("Enter the item you want to remove: ").strip()
            if item_to_remove in ordered_items:
                ordered_items.remove(item_to_remove)
                order_total -= Dishes_list[item_to_remove]
                print(f"Your item {item_to_remove} has been removed from your order list")
            else:
                print(f"Item {item_to_remove} is not in your order.")
        elif action != 'add':
            print("Invalid action. Please enter 'add' or 'remove'.")

# Final order summary
print("\nFinal Order Summary:")
display_order()
print(f"The Total Amount to pay is {order_total}.")

