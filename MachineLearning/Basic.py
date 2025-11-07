import pandas as pd

#Creating Data
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
# X Axis [Yes, No] Y Axis [0, 1]
#     Yes, No
# 0  [50, 131] 
# 1  [21,  2 ]

# Reading Data
wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv")

wine_reviews.head() 
# (129971, 14) # shape of the data (rows, columns)

# save filepath to variable for easier access
melbourne_file_path = '../sMachineLearning/melb_data.csv'
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path) 
# print a summary of the data in Melbourne data
melbourne_data.describe()

