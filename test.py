# Number of variables you want to create
num_variables = 5

# Use a for loop to create variables using exec()
for i in range(num_variables):
    variable_name = f"variable_{i}"
    variable_value = i * 2  # You can assign any value or expression here
    exec(f"{variable_name} = {variable_value}")

# Print the created variables
for i in range(num_variables):
    variable_name = f"variable_{i}"
    print(f"{variable_name} = {globals()[variable_name]}")
