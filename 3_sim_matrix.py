import pandas as pd
import numpy as np
from scipy.spatial.distance import cosine
from pandas import DataFrame

df_filter_user_ratings_ = pd.read_csv('csv_files/cos_sim_prep.csv')
df_filter_user_ratings_ = df_filter_user_ratings_.drop(['Unnamed: 0'], axis=1)
print(df_filter_user_ratings_.head(5))

a0 = pd.DataFrame()
for i in range(8):
    a1 = df_filter_user_ratings_.loc[df_filter_user_ratings_['user_id']==i]
    a1 = a1.rename(columns={'Assuming_Ratings': 'ratings'})
    a0 = pd.concat([a0, a1], axis=0)

df = a0.pivot(index='appid', columns='user_id', values='ratings')
print(df.head(5))
df.fillna(0.0, inplace = True)
df.to_csv('csv_files/df_fill_NA.csv')

similarity_matrix = pd.DataFrame(index=range(8), columns=range(8))

for i in range(8):
    for j in range(8):
        similarity_matrix.iloc[i, j] = 1 - cosine(df.iloc[:, i], df.iloc[:, j])
        
print(similarity_matrix)
similarity_matrix.to_csv('csv_files/sim_matrix.csv', index=True)
        