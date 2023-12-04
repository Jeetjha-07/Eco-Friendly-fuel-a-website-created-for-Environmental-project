# class EcoFriendlyFuelSystem:
#     def __init__(self):
#         self.fuel_types = {
#             'Biofuels': ['Ethanol', 'Biodiesel', 'Biogas'],
#             'Hydrogen': ['Electrolysis', 'Steam Methane Reforming'],
#             'Electric Vehicles': ['Battery Electric Vehicles (BEVs)', 'Plug-in Hybrid Electric Vehicles (PHEVs)']
#         }

#     def display_fuel_types(self):
#         print("Available Eco-Friendly Fuel Types:")
#         for fuel_category, types in self.fuel_types.items():
#             print(f"\n{fuel_category}:")
#             for fuel_type in types:
#                 print(f"  - {fuel_type}")

#     def calculate_emission_reduction(self, initial_emission, reduced_emission):
#         reduction_percentage = ((initial_emission - reduced_emission) / initial_emission) * 100
#         return round(reduction_percentage, 2)

# # Example Usage
# if __name__ == "__main__":
#     system = EcoFriendlyFuelSystem()

#     print("Welcome to the Eco-Friendly Fuel System!")
#     system.display_fuel_types()

#     # Simulating user input for emission reduction calculation
#     initial_emission = float(input("\nEnter the initial carbon emission (in CO2 equivalent) of your current fuel: "))
#     reduced_emission = float(input("Enter the reduced carbon emission (in CO2 equivalent) with the eco-friendly fuel: "))

#     reduction_percentage = system.calculate_emission_reduction(initial_emission, reduced_emission)

#     print(f"\nBy using eco-friendly fuel, you've reduced carbon emissions by {reduction_percentage}%.")
import json
import os
from datetime import datetime

class EcoFriendlyFuelOrderSystem:
    def __init__(self):
        self.fuels = {
            'Biofuels': {
                'Ethanol': 3.5,
                'Biodiesel': 4.0,
                'Biogas': 2.8
            },
            'Hydrogen': {
                'Electrolysis': 5.2,
                'Steam Methane Reforming': 6.0
            },
            'Electric Vehicles': {
                'BEVs': 0.25,
                'PHEVs': 0.35
            }
        }
        self.orders = []

    def display_fuel_types(self):
        print("Available Eco-Friendly Fuels:")
        for fuel_category, types in self.fuels.items():
            print(f"\n{fuel_category}:")
            for fuel_type, price_per_unit in types.items():
                print(f"  - {fuel_type} (${price_per_unit} per unit)")

    def place_order(self, fuel_type, quantity):
        if fuel_type in self.get_all_fuel_types() and quantity > 0:
            total_cost = self.fuels[fuel_type] * quantity
            order = {
                'fuel_type': fuel_type,
                'quantity': quantity,
                'total_cost': total_cost,
                'order_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.orders.append(order)
            print(f"Order placed successfully!\nTotal Cost: ${total_cost}")
        else:
            print("Invalid fuel type or quantity. Please check your input.")

    def view_order_history(self):
        if self.orders:
            print("\nOrder History:")
            for order in self.orders:
                print(f"\nFuel Type: {order['fuel_type']}")
                print(f"Quantity: {order['quantity']}")
                print(f"Total Cost: ${order['total_cost']}")
                print(f"Order Date: {order['order_date']}")
        else:
            print("No orders placed yet.")

    def get_all_fuel_types(self):
        return [fuel_type for fuel_category in self.fuels.values() for fuel_type in fuel_category]

    def save_orders_to_file(self):
        with open('order_history.json', 'w') as file:
            json.dump(self.orders, file, indent=2)
        print("Order history saved to 'order_history.json'.")

# Example Usage
if __name__ == "__main__":
    system = EcoFriendlyFuelOrderSystem()

    print("Welcome to the Eco-Friendly Fuel Order System!")
    system.display_fuel_types()

    fuel_type = input("\nEnter the eco-friendly fuel type you want to order: ")
    quantity = int(input("Enter the quantity you want to order: "))

    system.place_order(fuel_type, quantity)
    system.view_order_history()
    system.save_orders_to_file()

