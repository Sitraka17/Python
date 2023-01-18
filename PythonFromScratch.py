import pandas as pd
import seaborn as sns #the first words you will be able to read in any code is the import bloc. 
			    #when you start anything you need to prepare a frame and the tools. 
			    #packages are the tools, the ide is the frame. 

#A variable is usefull
#You will store informations. 

ur_first_variable = "an unremarkable string" 
#tada! It's stored!
#but be carefull. It will not be shown yet. 

name = "Isidora" 	# Declaring variable name
favorite_number = 12 	# Declaring variable favorite_number
#To see the variable in the console, you must call it. Using the print function! 
print(name) 		# Using variable name for a variable can be a string 
print(favorite_number) 	# Using variable number or a int/float. 

#But a variable can be changed before it's called. 
#then it will take the last known value. 
str1 = "na"
str2 = "ba"
str1 = str2
print(str1) 

#You can do computations (des calculs )
var1 = 7 
var2 = 6 
print (var1*var2) 

#You can concatenate strings 
var1 = "Gérard"
var2 = "Depardeux"
print (var1+" " + var2) 

#Python has a number of built-in functions for strings. 68 in 2023 [source]: https://www.codecademy.com/resources/docs/python/built-in-functions



###################### Level 2 ############
# Import pandas
import pandas as pd
# Load the 'ransom.csv' into a DataFrame
r = pd.read_csv('random.csv')

# Display DataFrame
print(r)
