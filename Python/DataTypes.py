# Integers
x = 14
print(x)
print(type(x))

# Floats
nearly_pi = 3.141592653589793238462643383279502884197169399375105820974944
print(nearly_pi)
print(type(nearly_pi))
# Round to 5 decimal places
rounded_pi = round(nearly_pi, 5)
print(rounded_pi)
print(type(rounded_pi))
y_float = 1.
print(y_float)
print(type(y_float))

#Booleans
z_one = True
print(z_one)
print(type(z_one))
z_two = False
print(z_two)
print(type(z_two))

# Strings
w = "Hello, Python!"
print(w)
print(type(w))
print(len(w))

# Question 1: 
# Define a float
y = 1.
print(y)
print(type(y))

# Convert float to integer with the int function
z = int(y)
print(z)
print(type(z))
# Uncomment and run this code to get started!
print(float(1.2321))
print(float(1.747))
print(float(-3.94535))
print(float(-2.19774))
# Question 2: 
# Uncomment and run this code to get started!
print(3 * False)
print(-3.1 * False)
print(type("abc" * False))
print(len("abc" * False))

# Question 3: 
# TODO: Complete the function
def get_expected_cost(beds, baths, has_basement):
    value = (80000 + (beds*30000) + (baths*10000)) + (40000 * has_basement)
    return value

# Check your answer 
q3.check()

# Question 4:
print(False + False)
print(True + False)
print(False + True)
print(True + True)
print(False + True + True + True)   
# Question 5:
def cost_of_project(engraving, solid_gold):
    num_units = len(engraving)
    
    # If it's solid gold
    if solid_gold:
        base_cost = 100
        cost_per_unit = 10
    else:
        base_cost = 50
        cost_per_unit = 7
    
    # Total cost = base + (per-unit × number of units)
    cost = base_cost + (cost_per_unit * num_units)
    
    return cost

# Check your answer
q5.check()