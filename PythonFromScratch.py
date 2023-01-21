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

#####      The 6 primitives of Turring    		######## 
#	Right: Move the Machine's head to the right of the current square.
#	Left: Move the Machine's head to the left of the current square.
#	Print: Print a symbol on the current square.
#	Scan: Identify any symbols on the current square.
#	Erase: Erase any symbols presented on the current square.
#	Halt: Do nothing.
#############################################################################

word = "learning"
print(word[1:5]) #Strings starts at 0 but a substring starts at 1 and ends at n+1 

word = "steamer"
start = 1
end = 5
print(word[start:end])


text = 'bat ball'

# REPLACE 'ba' with 'ro'
replaced_text = text.replace('ba', 'ro')
print(replaced_text)
# Output: rot roll


######### REPLACE FCTION ########
forecast = "It will be rainy today"
new_forecast = forecast.replace("rainy", "sunny")  #The REPLACE function returns a new string in which all instances of one substring are replaced with another substring.
print(forecast) # Original forecast
print(new_forecast) # New forecast

#LISTS / VARIABLES are useful in order to not type it every time. ie you store the informations in a variable so you can call it. 
words = "red fish"
words.replace("red", "blue")
print(words)
print(words.replace("red", "blue")) 
#in this example the variable words didn't saved the changes (just like in vidéo games)


form_letter = "Hello [Insert Name Here]. I'd like to personally thank you for your contribution." 
# Run the replacement to insert Emily
form_letter = form_letter.replace("[Insert Name Here]", "Emily in Paris")
# Print the updated letter
print(form_letter)



###################### Level 2 ############
# Import pandas
import pandas as pd
# Load the 'random.csv' into a DataFrame
r = pd.read_csv('random.csv')

# Display DataFrame
print(r)
# Plot a graph
plt.plot(x_values, y_values)

# Display the graph
plt.show()


########################## Level 3 #########
