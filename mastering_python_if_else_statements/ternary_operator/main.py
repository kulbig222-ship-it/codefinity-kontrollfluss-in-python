water_intake = 1.9
# Example value
true_message = "You've met your hydration goal!"
false_message = "Drink more water to reach your goal."

# Using ternary operator to check hydration goal
message = true_message if water_intake >= 2.0 else false_message

# Testing
print("Hydration Status:", message)