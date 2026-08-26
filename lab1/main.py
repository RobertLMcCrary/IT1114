# Program Name: lab1.py
# Course: IT1114/Section XXX
# Student Name: Robert McCrary
# Assignment Number: Lab#
# Due Date: 08/27/2026
# Purpose: 
# 

width = float(input("Room Width: "))
length = float(input("Room Length: "))
cost = float(input("Cost per Sq. Foot: "))

tax = 0.07 * cost
total_cost_pre_tax = (width * length) * cost
total_cost = (tax + cost) * (width * length)

print(f"Square feet: {width * length}")
print(f"Flooring: {total_cost_pre_tax}")
print(f"Tax: {tax}")
print(f"Total: {total_cost}")
