# Define Functions 
def add_three(input_var):
    output_var = input_var + 3
    return output_var


# Question 1: 
def get_expected_cost(beds, baths):
    value = 80000 + (30000*beds) + (10000*baths)
    return value

# Question 2: 
# TODO: Use the get_expected_cost function to fill in each value
option_one = get_expected_cost(2,3)
option_two = get_expected_cost(3,2)
option_three = get_expected_cost(3,3)
option_four = get_expected_cost(3,4)

print(option_one)
print(option_two)
print(option_three)
print(option_four)

# Question 3: 
def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    cost = ((sqft_walls + sqft_ceiling) / sqft_per_gallon) * cost_per_gallon
    return cost

# Question 4: 
def get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    cost = math.ceil((sqft_walls + sqft_ceiling) / sqft_per_gallon) * cost_per_gallon
    return cost

# Question 5: 


