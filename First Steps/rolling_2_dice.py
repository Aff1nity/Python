

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

for roll_num in range(10000):
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

# Now that everyting works correctly, I would like to have an overview of the average damage
# that my party has in order to build better and balanced encounters

# Party: 1. Narayan, Monk. 2, 3 and 4 attacks possible. Damage: 1d6+4 per attack
#        2. Gloomwood, Ranger. 2 and 3 attacks possible. Damage: 1d8+5 per attack + 1d6 hunter's mark
#        3. Rocco, Rogue. 1 attack possible + sneak attack (lvl7). Damage: 2d6+4 per attack + 4d6
#        4. Bilbron, Wizard, swordsinger. 1 attack possible. Damage: 1d6+3 per attack + 2d6 extra damage

# Summary: 1 = 2d6, 3d6, 4d6 +4
#          2 = 2d8, 2d6 +5
#          3 = 6d6 + 4
#          2 = 3d6 + 3

# 1. Narayan

#Create four 4d for maximun damage
die_1 = Die()
die_2 = Die()
die_3 = Die()
die_4 = Die()

#Adding +16 at the end since Narayan has +4 per hit.

results_narayan = []

for roll_num in range(100000):
    result = die_1.roll() + die_2.roll() + die_3.roll() + die_4.roll()
    results_narayan.append(result)

#Analyzing the results: Counting the value of each result

frequencies = []
max_range = die_1.num_sides + die_2.num_sides + die_3.num_sides + die_4.num_sides
count_results = range(1, max_range+1)
for value in count_results:
    frequency = results_narayan.count(value)
    frequencies.append(frequency)

#Visualizing the results and customizing the plot
title = "Narayan: Result of rolling four D6 1,000 times"
labels = {'x': 'Results', 'y': 'Frequency of results'}
px.bar(x=count_results, y=frequencies, title=title, labels=labels)

# Average = 16 damage per round + 16 = 32dps
#############################################################################################
# 2. Gloomwood

#Create two 4d for maximun damage
die_1 = Die(8)
die_2 = Die(8)
die_3 = Die()
die_4 = Die()

#Adding +10 at the end since Gloomwood has +5 per hit.

results_gw = []

for roll_num in range(100000):
    result = die_1.roll() + die_2.roll() + die_3.roll() + die_4.roll()
    results_gw.append(result)
print(results_gw)
#Analyzing the results: Counting the value of each result

frequencies = []
max_range = die_1.num_sides + die_2.num_sides + die_3.num_sides + die_4.num_sides
count_results = range(4, max_range+1)
for value in count_results:
    frequency = results_gw.count(value)
    frequencies.append(frequency)

#Visualizing the results and customizing the plot
title = "Gloomwood: Result of rolling two D6 and two d8 1,000 times"
labels = {'x': 'Results', 'y': 'Frequency of results'}
px.bar(x=count_results, y=frequencies, title=title, labels=labels)

# Average = 16 damage per round + 10 = 26dps

#############################################################################################
# 3. Rocco

#Create two 6d for maximun damage
die_1 = Die()
die_2 = Die()
die_3 = Die()
die_4 = Die()
die_5 = Die()
die_6 = Die()

#Adding +4 at the end since Rocco has +4 per hit.

results_rocco = []

for roll_num in range(100000):
    result = die_1.roll() + die_2.roll() + die_3.roll() + die_4.roll() + die_5.roll() + die_6.roll() + 4
    results_rocco.append(result)

#Analyzing the results: Counting the value of each result

frequencies = []
max_range = die_1.num_sides + die_2.num_sides + die_3.num_sides + die_4.num_sides + die_5.num_sides + die_6.num_sides
count_results = range(6, max_range+4)
for value in count_results:
    frequency = results_rocco.count(value)
    frequencies.append(frequency)

#Visualizing the results and customizing the plot
title = "Rocco: Result of rolling six 6d6 1,000 times"
labels = {'x': 'Results', 'y': 'Frequency of results'}
px.bar(x=count_results, y=frequencies, title=title, labels=labels)

# Average = 27 damage per round + 4 = 31dps

#############################################################################################
# 4. Bilbron

#Create three 6d for maximun damage
die_1 = Die()
die_2 = Die()
die_3 = Die()

#Adding +9 at the end since Bilbron has +3 per hit.

results_bilbron = []

for roll_num in range(100000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results_bilbron.append(result)

#Analyzing the results: Counting the value of each result

frequencies = []
max_range = die_1.num_sides + die_2.num_sides + die_3.num_sides
count_results = range(3, max_range+1)
for value in count_results:
    frequency = results_bilbron.count(value)
    frequencies.append(frequency)
print(frequencies)
#Visualizing the results and customizing the plot
title = "Bilbron: Result of rolling three 3d6 1,000 times"
labels = {'x': 'Results', 'y': 'Frequency of results'}
px.bar(x=count_results, y=frequencies, title=title, labels=labels)

# Average = 10-11 damage per round + 3 = 15dps

# Conclusion: The average full damage that the party can deal is: 104
# In the likely event that every PC lands every hit, any boss that I create should have at least
# more than 100HP if I want it to live for more than one round.
