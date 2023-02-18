
import matplotlib.pyplot as plt

from pathlib import Path
import csv

path = Path('C:\Python\Projects\sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#Print each header and its position in the list to make it easier to understand
reader = csv.reader(lines)
for index, column_header in enumerate(header_row):
    print(index, column_header)

#Extracting and reading data using the previous index generated
#Extract high temperatures
highs = []
for row in reader:
    high = row[4]
    highs.append(high)
#Removing first item as it is not an integer
del highs[0]
print(highs)

#Converting the data to Celsius
highs_in_celcius = []

for value in highs:
    celcius = (int(value) - 32)/1.8
    celcius = round(celcius, 2)
    highs_in_celcius.append(celcius)

print(highs_in_celcius)

#Plotting data in a temperature chart
ax = plt.subplot()
ax.plot(highs_in_celcius, color='red')

#Formatting the plot
ax.set_title("Daily high temperatures, July 2021", fontsize=22)
ax.set_xlabel('', fontsize=15)
ax.set_ylabel('Temperature(C)', fontsize=15)
ax.tick_params(labelsize=15)

