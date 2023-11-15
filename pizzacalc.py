import math
import tkinter as tk
from tkinter import ttk

def calculate_area(radius):
    return math.pi * (radius ** 2)  # Area of a circle

def calculate_price_per_inch2(price, area):
    return price / area

def compare_pizzas():
    pizza1_name = pizza1_name_entry.get()
    pizza1_price = float(pizza1_price_entry.get())
    pizza1_diameter = float(pizza1_diameter_entry.get())

    pizza2_name = pizza2_name_entry.get()
    pizza2_price = float(pizza2_price_entry.get())
    pizza2_diameter = float(pizza2_diameter_entry.get())

    # Convert diameter from inches to radius
    pizza1_radius = pizza1_diameter / 2
    pizza2_radius = pizza2_diameter / 2

    # Calculate areas
    area1 = calculate_area(pizza1_radius)
    area2 = calculate_area(pizza2_radius)

    # Calculate price per in²
    price_per_inch2_1 = calculate_price_per_inch2(pizza1_price, area1)
    price_per_inch2_2 = calculate_price_per_inch2(pizza2_price, area2)

    # Display results
    result_label.config(text=f"{pizza1_name} price per in²: £{price_per_inch2_1:.2f}\n"
                             f"{pizza2_name} price per in²: £{price_per_inch2_2:.2f}\n\n"
                             f"The best deal is {pizza1_name}!" if price_per_inch2_1 < price_per_inch2_2
                             else f"The best deal is {pizza2_name}!" if price_per_inch2_1 > price_per_inch2_2
                             else "Both pizzas have the same price per in².")

# Create the main window
window = tk.Tk()
window.title("Pizza Price Comparison")

# Create and place widgets
pizza1_label = ttk.Label(window, text="Pizza 1:")
pizza1_name_label = ttk.Label(window, text="Name:")
pizza1_price_label = ttk.Label(window, text="Price (GBP):")
pizza1_diameter_label = ttk.Label(window, text="Diameter (in):")

pizza1_name_entry = ttk.Entry(window)
pizza1_price_entry = ttk.Entry(window)
pizza1_diameter_entry = ttk.Entry(window)

pizza2_label = ttk.Label(window, text="Pizza 2:")
pizza2_name_label = ttk.Label(window, text="Name:")
pizza2_price_label = ttk.Label(window, text="Price (GBP):")
pizza2_diameter_label = ttk.Label(window, text="Diameter (in):")

pizza2_name_entry = ttk.Entry(window)
pizza2_price_entry = ttk.Entry(window)
pizza2_diameter_entry = ttk.Entry(window)

compare_button = ttk.Button(window, text="Compare", command=compare_pizzas)
result_label = ttk.Label(window, text="Results will be displayed here.")

# Grid layout
pizza1_label.grid(row=0, column=0, columnspan=2, pady=(10, 5))
pizza1_name_label.grid(row=1, column=0, sticky="e")
pizza1_name_entry.grid(row=1, column=1)
pizza1_price_label.grid(row=2, column=0, sticky="e")
pizza1_price_entry.grid(row=2, column=1)
pizza1_diameter_label.grid(row=3, column=0, sticky="e")
pizza1_diameter_entry.grid(row=3, column=1)

pizza2_label.grid(row=0, column=2, columnspan=2, pady=(10, 5))
pizza2_name_label.grid(row=1, column=2, sticky="e")
pizza2_name_entry.grid(row=1, column=3)
pizza2_price_label.grid(row=2, column=2, sticky="e")
pizza2_price_entry.grid(row=2, column=3)
pizza2_diameter_label.grid(row=3, column=2, sticky="e")
pizza2_diameter_entry.grid(row=3, column=3)

compare_button.grid(row=4, column=0, columnspan=4, pady=(10, 5))
result_label.grid(row=5, column=0, columnspan=4, pady=(5, 10))

# Start the main event loop
window.mainloop()
