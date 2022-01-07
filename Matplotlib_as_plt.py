################################################
# Import package                               #
                                               #
import matplotlib.pyplot as plt                #
                                               #
# Build Scatter plot                           #
plt.scatter(x,y)                               #
                                               #
# Show plot                                    #
plt.show()                                     #
############################################## #


# Print the last item from year and pop

print(year[-1])
print(pop[-1])

# Import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
# Make a line plot: year on the x-axis, pop on the y-axis

plt.plot(year,pop)
# Display the plot with plt.show()
plt.show()

#https://matplotlib.org/
import numpy as np
import matplotlib.pyplot as plt

# this sets up the Matplotlib interactive windows:
%matplotlib widget

# this changes the default date converter for better interactive plotting of dates:
plt.rcParams['date.converter'] = 'concise'

# Build histogram with 5 bins
plt.hist(life_exp,5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp,20)

# Show and clean up again
plt.show()
plt.clf()


# Scatter plot
plt.scatter(gdp_cap, life_exp)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val,tick_lab)

# After customizing, display the plot
plt.show()


# Import numpy as np

import numpy as np
# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop= np_pop*2
# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = pop)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()


