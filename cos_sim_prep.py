import pandas as pd
import numpy as np
from scipy.spatial.distance import cosine
from pandas import DataFrame

df_user_ratings = pd.read_csv('user_ratings.csv')
df_filter_user_ratings = df_user_ratings[['user_id','appid','Assuming_Ratings']]
df_filter_user_ratings.to_csv('filter_user_ratings')

df_filter_user_ratings_ = pd.read_csv('filter_user_ratings')
df_filter_user_ratings_.head(5)
df_filter_user_ratings_ = df_filter_user_ratings_.drop(['Unnamed: 0'], axis=1)

a0 = pd.DataFrame()
for i in range(8):
    #a0 = user_rating_df.loc[user_rating_df['user_id']==0]
    #a0 = a0.rename(columns={'Assuming_Ratings': 0})
    #a0 = a0.drop(['user_id'], axis=1)
#aa = a0.set_index('appid', inplace=True)
    a1 = df_filter_user_ratings_.loc[df_filter_user_ratings_['user_id']==i]
    a1 = a1.rename(columns={'Assuming_Ratings': 'ratings'})
    #a1 = a1.drop(['user_id'], axis=1)
#a1 = a1.set_index('appid', inplace=True)
    
    a0 = pd.concat([a0, a1], axis=0)