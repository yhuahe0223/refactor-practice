from budget import suggest_destination 
from calculator import calculator
from weather import WeatherAssistant
from shoppingList import ShoppingList
from TemperatureConverter import celsius_to_fahrenheit 
from TemperatureConverter import fahrenheit_to_celsius
from inventory import inventoryList
from passwordChecker import validate_password
suggest_destination(300)

calculator(10,1)

WeatherAssistant('rainy')

ShoppingList('Pineapple')

celsius_to_fahrenheit('23')

fahrenheit_to_celsius('23')

inventoryList('carrot')

validate_password('123456')



# Instructions for Students:

# Refactor this code by creating a function for each arithmetic operation (e.g., add, subtract, etc.).
# Make a Calculator class that contains these functions as methods.
# Ensure that division checks for zero before attempting the operation.
# Move the arithmetic logic into a file named calculator.py.

    

####################################################################################################
# Instructions for Students:

# Create a function that takes weather as an argument and returns the appropriate advice.
# Optionally, create a class WeatherAssistant with a method for weather advice.
#Move the weather advice logic into a file named weather_advice.py.



# Instructions for Students:

# Refactor this code by creating functions to:
# Add an item to the shopping list.
# Remove an item from the shopping list.
# Print all items in the shopping list.
# Optionally, create a ShoppingList class that manages the list with the above methods.
#Move the shopping list logic into a file named shopping_list.py.


# Instructions for Students:

# Refactor this code by creating two functions:
# celsius_to_fahrenheit(celsius)
# fahrenheit_to_celsius(fahrenheit)
# Consider creating a TemperatureConverter class with these methods.







# Instructions for Students:

# Create functions for:
# Adding an item to the inventory.
# Removing an item from the inventory.
# Printing the inventory.
# Optionally, organize these into an Inventory class.








# Instructions for Students:

# Refactor this code by creating a validate_password(password) function.
# Extend it to check for additional rules like special characters.
