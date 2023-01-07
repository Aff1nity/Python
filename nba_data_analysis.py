

import pandas as pd
import seaborn as sns
import numpy as np

import matplotlib.pyplot as plt

plt.style.use('Solarize_Light2')
from matplotlib import figure

#Read in the data

df = pd.read_csv(r"C:\Python\Projects\NBAstats\Team Totals.csv")

df.head()

#Checking eachteam appereance in playoffs
df1 = pd.DataFrame(df, columns=['team', 'playoffs','season'])

df2 = df1.groupby(['team'])['playoffs'].count().sort_values(ascending=False).reset_index()
print(df2)

#Visualizing the results
plt.scatter(x = df2['playoffs'].head(30), y = df2['team'].head(30))

plt.setp(plt.xticks()[1], rotation=30, ha='right')
plt.show()
#I was not expecting to see the New York Knicks with the same amount of appearences as Boston

#I would like to compare the best team and team number 30 in the previous dataframe
#Boston Celtics vs Charlotte Hornets

df_poss = pd.read_csv(r"C:\Python\Projects\NBAstats\Team Stats Per 100 Poss.csv")

boston_vs_charlotte = df_poss.loc[df_poss['team'].isin(['Charlotte Hornets','Boston Celtics'])]
#new = boston_vs_charlotte.groupby(['team']).count()
print(boston_vs_charlotte)

