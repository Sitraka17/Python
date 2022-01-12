# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']
# Get index of 'germany': ind_ger
ind_ger= countries.index('germany')
# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])


# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = { 'spain':'madrid','france':'paris', 'germany':'berlin','norway':'oslo' }

# Print europe
print(europe)

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe['norway'])

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe["germany"] = 'berlin'

# Remove australia
del(europe["australia"])

# Print europe
print(europe)

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france'])
# Create sub-dictionary data
data={'capital': 'rome', 'population': 59.83}
# Add data to europe under key 'italy'
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } ,
           'italy':{'capital': 'rome', 'population': 59.83}}
# Print europe
print(europe)


#############################################
dict = {
"country":["Brazil","Russia","India","China","South Africa"],
"capital":["Brasilia","Moscow","New Delhi","Beijing","Pretoria"],
"area":[8.516, 17.10, 3.286, 9.597, 1.221]
"population":[200.4, 143.5, 1252, 1357, 52.98] }
####################################################### thus { then "key":[ "names"], again , finaly } 
#Pandas is a HIGH level #
#########################

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd 

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {
    "country":names, "drivers_right":dr,"cars_per_cap":cpc }
# it's not 'names' since it's a variable
#it's not [names] since it's not a list but a variable

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)
# Print cars
print(cars)
