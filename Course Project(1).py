#Jenny's Pizzeria Delivery Service

import datetime
import tkinter as tk
from pizza_module import Pizza, select_pizza, select_toppings, select_delivery_time

#Function that adds pizza order to receipt file
def place_order(pizza, delivery_time):
    file_name = "pizza_order_receipt.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write("Pizza Order Summary:\n")
        file.write(f"Pizza: {pizza}\n")
        file.write(f"Toppings: {', '.join(pizza.toppings)}\n")
        formatted_time = delivery_time.strftime('%Y-%m-%d %H:%M')
        file.write(f"Delivery Time: {formatted_time}\n")
    
    print(f"Order placed successfully. Here's your receipt.")
    
#Function to display tkinter image 
def show_picture():
    root = tk.Tk()
    logo = tk.PhotoImage(file="pic.gif")
    
    w1 = tk.Label(root, image=logo)
    w1.pack(side='right')
    
    root.mainloop()

#Function that manages the pizza ordering proccess
def main():
    print("Welcome to Jenny's Pizzeria! Choose a pizza from the menu to get started on your order.")
    
    while True:
        #Pizza Menu Options
        menu = [
            Pizza("Cheese", "Small", 10.99),
            Pizza("Pepperoni", "Extra Large", 16.99),
            Pizza("Meat Lovers", "Large", 20.99),
            Pizza("Deep Dish Special", "Medium", 9.99),
            Pizza("Vegetarian", "Medium", 11.99)
        ]

        # Available Delivery Times
        delivery_times = [
            datetime.datetime(2024, 8, 1, 12, 0),
            datetime.datetime(2024, 8, 1, 13, 0),
            datetime.datetime(2024, 8, 1, 14, 30),
            datetime.datetime(2024, 8, 1, 15, 0)
        ]

        try:
            # Select a pizza from the menu
            pizza = select_pizza(menu)

            # Select toppings for pizza
            select_toppings(pizza)

            # Select preferable delivery time
            delivery_time = select_delivery_time(delivery_times)
            place_order(pizza, delivery_time)

            # Ask customer if they want to place a new order
            new_order = input("Would you like to place a new order? (yes/no): ").lower()
            if new_order != 'yes':
                break
        
        except ValueError as ve:
            print(f"ValueError: {ve}") 
        except Exception as e:
            print(f"An error occurred: {e}")

    print("Thank you for visiting Jenny's Pizzeria. Have a great day!")
    show_picture()  # Display pizza picuture 


if __name__ == "__main__":
    main()
