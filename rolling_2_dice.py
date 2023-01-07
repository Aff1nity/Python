

import plotly.express as px
from random import randint

#Create a class for rolling dice

class Die:
    """"A class representing a die."""

    def __init__(self, num_side=6):
        
        self.num_sides = num_side
        
    def roll(self):
        """"Return a random value between 1 and 6."""
        return randint(1, self.num_sides)


#Create two d6.
die_1 = Die()
die_2 = Die()

#Make some rolls and store in a list

results = []

for roll_num in range(100000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#Analyzing the results: Counting the value of each result

frequencies = []
max_range = die_1.num_sides + die_2.num_sides
count_results = range(2, max_range+1)
for value in count_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualizing the results and customizing the plot
title = "Result of rolling two D6 1,000 times"
labels = {'x': 'Results', 'y': 'Frequency of results'}
px.bar(x=count_results, y=frequencies, title=title, labels=labels)

