import pandas as pd
import numpy as np
from scipy.spatial.distance import cosine
from pandas import DataFrame

df_user_ratings = pd.read_csv('user_ratings.csv')
df_filter_user_ratings = df_user_ratings[['user_id','appid','Assuming_Ratings']]
df_filter_user_ratings.to_csv('cos_sim_prep.csv')
