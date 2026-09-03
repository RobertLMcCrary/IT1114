# Program Name: Lab1.py
# Course: IT1114 and IT1114L Section 01
# Student Name: Robert McCrary
# Assignment Number: Lab1
# Due Date: 09/5/2026
# Editor: Neovim
# Environment: Nix
# GitHub: https://github.com/RobertLMcCrary/IT1114

# take user input as a float
width = float(input("Room Width: "))
length = float(input("Room Length: "))
cost = float(input("Cost per Sq. Foot: "))

# compute values
sq_ft = length * width
cost_pre_tax = cost * sq_ft
tax = cost_pre_tax * 0.07
cost_post_tax = cost_pre_tax + tax

# display correct output
print(f"Square feet: {sq_ft}")
print(f"Flooring: {cost_pre_tax}")
print(f"Tax: {tax}")
print(f"Total: {cost_post_tax}")
