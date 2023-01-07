
#Import libraries
import pandas as pd
import seaborn as sns
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib import figure

#%matplotlib inline
#Adjusting the configration of the plots
matplotlib.rcParams['figure.figsize'] = (12,8) 

#Read in the data

df = pd.read_csv(r"C:\Python\Projects\movie_dataset\movies_1.csv")

#Quick glance at the dataset
df.head()

#Is there any missing data?
for column in df.columns:
    porcentaje_missing = np.mean(df[column].isnull())
    #porcentaje_missing = round(porcentaje_missing, 2)
    print(f'{column} {round(porcentaje_missing, 1)}%')

#Looks good to use
#Checking datatypes 
print(df.dtypes)

#Order columns
df.sort_values(by=['budget'], inplace=False, ascending=False)

#Drop duplicates
df.drop_duplicates()

#Checking for correlation: Budget vs Gross
plt.figure(figsize=(15,10))
plt.scatter(x=df['budget'], y=df['gross'])

plt.title('Budget vs Gross Earnings')
plt.xlabel('Gross Earnings')
plt.ylabel('Budget for Film')

#Regression plot to confirm hyphotesys
sns.regplot(x='budget', y='gross', data=df, scatter_kws={'color':'blue'})
#plt.show()

#Positive correlation. Let's see how much is it.
df.corr( method='pearson', min_periods=1, numeric_only=True)

#High correclation between budget and gross: 0.740395

correlation_matrix = df.corr( method='pearson', min_periods=1, numeric_only=True)

sns.heatmap(correlation_matrix, annot=True)
plt.show()

# Conclusions: It seems that budget has a strong correlation 
# with gross revenue as expected. Further, it seems that votes
# also have a strong correlation with gross revenaue.

# I would like to see the revenue gross earned by each genre

x = df['genre']
y = df['gross']

fig = plt.figure(figsize = (15, 5))

plt.barh(x, y, color = 'green')
plt.title('Gross by Genre')
plt.xlabel('Genres', fontsize=5)
plt.ylabel('Gross Revenue', fontsize=15)

plt.show()
