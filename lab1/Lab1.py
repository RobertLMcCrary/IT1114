# Program Name: Lab1.py
# Course: IT1114 and IT1114L Section 01
# Student Name: Robert McCrary
# Assignment Number: Lab1
# Due Date: 08/27/2026
# Editor: Neovim
# Env: Nix

# take user input as a float
width = float(input("Room Width: "))
length = float(input("Room Length: "))
cost = float(input("Cost per Sq. Foot: "))

# compute values
tax = 0.07 * cost
total_cost_pre_tax = (width * length) * cost
total_cost = (tax + cost) * (width * length)

# display correct output
print(f"Square feet: {width * length}")
print(f"Flooring: {total_cost_pre_tax}")
print(f"Tax: {tax}")
print(f"Total: {total_cost}")
