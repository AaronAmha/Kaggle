#If Statements

def evaluate_temp(temp):
    # Set an initial message
    message = "Normal temperature."
    # Update value of message only if temperature greater than 38
    if temp > 38:
        message = "Fever!"
    return message
def evaluate_temp_with_else(temp):
    if temp > 38:
        message = "Fever!"
    else:
        message = "Normal temperature."
    return message
def evaluate_temp_with_elif(temp):
    if temp > 38:
        message = "Fever!"
    elif temp > 35:
        message = "Normal temperature."
    else:
        message = "Low temperature."
    return message

def get_taxes(earnings):
    if earnings < 12000:
        tax_owed = .25 * earnings
    else:
        tax_owed = .30 * earnings
    return tax_owed

# Question 1:
# TODO: Edit the function to return the correct grade for different scores
def get_grade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade =  "B"
    elif score >= 70:
        grade =  "C"
    elif score >= 60:
        grade =  "D"
    else:
        grade =  "F"
    return grade
    
# Check your answer
q1.check()
# Question 2: 
def cost_of_project(engraving, solid_gold):
    if solid_gold == True:
        cost = (len(engraving) * 10) + 100
    else:
        cost = (len(engraving) * 7) + 50
    return cost

# Check your answer
q2.check()

# Question 3: 
# Question 4: 
# Question 5: