
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


#Create a d6.
die = Die()

#Make some rolls and store in a list

results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#Analyzing the results: Counting the value of each result

frequencies = []
count_results = range(1, die.num_sides+1)
for value in count_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#Show each number with its result.
print(f'Number 1: {frequencies[0]} \nNumber 2: {frequencies[1]}\nNumber 3: {frequencies[2]}\nNumber 4: {frequencies[3]}\nNumber 5: {frequencies[4]}\nNumber 6: {frequencies[5]}')

#Visualizing the results and customizing the plot
title = "Result of rolling One D6 1,000 times"
labels = {'x': 'Results', 'y': 'Frequency of results'}
px.bar(x=count_results, y=frequencies, title=title, labels=labels)

