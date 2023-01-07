
from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path("C:\Python\Projects\weather_data\sitka_weather_2021_full.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Cheking index position of the column I am going to use
for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract high temperatures and dates

dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = (row[7])
    low = (row[8])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)
#Removing an invalid input: Empty value and adding the correct value
highs.pop(112)
highs.insert(22, 112)
len(lows)

# Converting Fahrenheit to Celcius
highs_celcius = []
lows_celcius = []

#Future: Convert to function
for celcius in highs:
    temp_celcius = (int(celcius) - 32 )/ 1.8
    highs_celcius.append(round(temp_celcius, 1))

for celcius in lows:
    temp_celcius = (int(celcius) - 32 )/ 1.8
    lows_celcius.append(round(temp_celcius, 1))

# Plot high temperatures and low temperatures
fig, ax = plt.subplots()
ax.plot(dates, highs_celcius, color = 'red')
ax.plot(dates, lows_celcius, color = 'blue')

ax.set_title('Daily High and Low Temperatures', fontsize=20)
ax.set_xlabel('', fontsize=15)
fig.autofmt_xdate()
ax.set_ylabel('Temperature(F)', fontsize=5)
ax.tick_params(labelsize=12)

plt.show()
