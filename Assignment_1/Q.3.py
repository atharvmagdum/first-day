# a) Read CSV File
import pandas as pd
data = pd.read_csv('Assignment 1\products.csv')

# b) Print each row in a clean format
print(data)

# c) Total number of rows
total_rows = len(data)
print("\nTotal rows are : ",total_rows)

# d) Total number of products priced above 500
above_500 = data[data["price"] > 500]
print("\nProducts Priced above 500 :",len(above_500))

# e) Average price of all products 
average_price = data["price"].mean()
print("\nAverage price of all products :",average_price)

# Day 3 Wifi Password : j8uzbj2h

# f) List all products belonging to a specific category (user input)
category = input("Enter the category to print :")
filtered = data[data["category"].strlower() == category.lowe()]
print("Data inside given category :", category , ":")
print(filtered)

# g) Total quantity of all items in stock
total_quantity = data[data["quantity"]].sum()
print("Total Available Stock Quantity :",total_quantity)