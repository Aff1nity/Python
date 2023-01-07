

import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1, 4, 9, 16, 25]

#Selecting a style
plt.style.use('Solarize_Light2')

#Set plot color to green
fig, ax = plt.subplots()
ax.plot(input_values, squares, color='green', linewidth=3)

#Set chart title and label axes.
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

#Set size of tick labels.
ax.tick_params(labelsize=14)

plt.show()

#Using a series of points with scatter()
#Auto generate square values on y axis by looping through a list
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

#Trying a color map
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

#Set the chart titles and labels using a smaller size due to the large dataset generated
ax.set_title('Square Numbers', fontsize=20)
ax.set_xlabel('Value', fontsize=10)
ax.set_ylabel('Square of Value', fontsize=10)

#Specify the range for each axis
ax.axis(0, 1100, 0, 1100000)

plt.show
