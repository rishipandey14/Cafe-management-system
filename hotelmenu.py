from prettytable import PrettyTable

Dishes_list = {
    'Pizza':200,
    'Pasta':100,
    'Burger':50,
    'Chowmean':40,
    'aaloo tikki':40,
    'Pakodi':30,
    'Aaloo chop':50,
    'Spring roll':40,
}

# Greet
print("\n Welcome to RR (Rishi Restaurant)\n")

# Define the menu of restaurant
# These 3 are the columns of the tables
menu = PrettyTable(['Sr.no', 'Dish', 'Price'])
 
# To insert rows:
menu.add_row(['1', 'Pizza', 200])
menu.add_row(['2', 'Pasta', 100])
menu.add_row(['3', 'Burger', 50])
menu.add_row(['4', 'Chowmean', 40])
menu.add_row(['5', 'Aaloo tikki', 40])
menu.add_row(['6', 'Pakodi', 30])
menu.add_row(['7', 'Aaloo chop', 50])
menu.add_row(['8', 'Spring roll', 40])
 
print(menu)







