################################################
# Import package

import matplotlib.pyplot as plt

# Build Scatter plot
plt.scatter(x,y)

# Show plot
plt.show()
##############################################


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




