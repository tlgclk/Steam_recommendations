import json
from urllib.request import urlopen
import requests,json,os,sys,time,re
import pandas as pd
import numpy as np
# Boş bir DataFrame oluştur
df_user_links = pd.DataFrame(columns=['Links'])

# Yeni satırları bir liste olarak tanımla
new_rows = [
    {'Links': 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=12342C69B72B036F8E660D95F28DF431&steamid=76561197960434622&format=json'},
    {'Links': 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=12342C69B72B036F8E660D95F28DF431&steamid=76561198016215597&format=json'},
    {'Links': 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=12342C69B72B036F8E660D95F28DF431&steamid=76561198202525417&format=json'},
    {'Links': 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=12342C69B72B036F8E660D95F28DF431&steamid=76561198089202086&format=json'},
    {'Links': 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=12342C69B72B036F8E660D95F28DF431&steamid=76561198029242928&format=json'},
    {'Links': 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=12342C69B72B036F8E660D95F28DF431&steamid=76561198014403181&format=json'},
    {'Links': 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=12342C69B72B036F8E660D95F28DF431&steamid=76561198207433511&format=json'},
    {'Links': 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=12342C69B72B036F8E660D95F28DF431&steamid=76561197966611389&format=json'},
    {'Links': 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=12342C69B72B036F8E660D95F28DF431&steamid=76561198077345441&format=json'},
    {'Links': 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=12342C69B72B036F8E660D95F28DF431&steamid=76561198089768783&format=json'},
    {'Links': 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=12342C69B72B036F8E660D95F28DF431&steamid=76561198024696613&format=json'}
]

# Listeyi DataFrame'e dönüştür ve mevcut DataFrame ile birleştir
df_user_links = pd.concat([df_user_links, pd.DataFrame(new_rows)], ignore_index=True)

# Sonuçları göster
print(df_user_links)

game_play_median = pd.read_csv('filtered_steam.csv')

columns = [
    'appid', 
    'playtime_forever', 
    'playtime_2weeks', 
    'name', 
    'median_playtime', 
    'Assuming_Ratings', 
    'user_id'
]

try:
    user_ratings = pd.read_csv('user_ratings.csv')
except FileNotFoundError:
    # Dosya bulunamazsa boş bir DataFrame oluştur
    user_ratings = pd.DataFrame(columns=columns)

    # Dosyayı oluştur
    user_ratings.to_csv('user_ratings.csv', index=False)

def get_df(aa):
    ss = aa.json()
    sd = pd.DataFrame(ss['response']['games'])
    #sd.drop(sd.columns[[1,3, 4, 5]], axis = 1, inplace = True)



    no_zero = sd.loc[sd['playtime_forever']!=0]
#ddf_col = pd.concat([aaaa,game_play_median], axis=1)
    df_col = pd.merge(no_zero, game_play_median, on="appid")
    return df_col

def get_ratings(df_col):
    df_col['Assuming_Ratings'] = 0
    for i in range(len(df_col)):
        if df_col['playtime_forever'][i]>= df_col['median_playtime'][i]:
            df_col['Assuming_Ratings'][i] = 5
    #else:
     #   df_col['Assuming_Ratings'][i] = 2
        elif df_col['median_playtime'][i]>df_col['playtime_forever'][i]>= df_col['median_playtime'][i]*0.8:
            df_col['Assuming_Ratings'][i] = 4
        elif df_col['median_playtime'][i]*0.8>df_col['playtime_forever'][i]>= df_col['median_playtime'][i]*0.5:
            df_col['Assuming_Ratings'][i] = 3
        elif df_col['median_playtime'][i]*0.5>df_col['playtime_forever'][i]>= df_col['median_playtime'][i]*0.1:
            df_col['Assuming_Ratings'][i] = 2
        elif df_col['median_playtime'][i]*0.1>df_col['playtime_forever'][i]:
            df_col['Assuming_Ratings'][i] = 1
    return df_col

def current_user_id(df):
    if len(df) == 0:
        return 0
    current_user_id = df['user_id'].max()
    return current_user_id

def RDD_csv(df_col,i):
    df_col_text = df_col
    df_col_text['user_id'] = current_user_id(user_ratings) + i
    return df_col_text

df_col_text_ = []
df_col_a1 = get_ratings(get_df(requests.get(df_user_links['Links'][0])))
df_col_text_ = RDD_csv(df_col_a1,0)

df_col_text_ = df_col_text_.drop(df_col_text_.index[0:len(df_col_text_)],axis = 0) 
df_col_text_

for i in range(8):
    
    df_col_ = get_ratings(get_df(requests.get(df_user_links['Links'][i])))    ###### Anti_crawler when i >= 9
    df_col_text_element = RDD_csv(df_col_,i)
    df_col_text_ = pd.concat([df_col_text_, df_col_text_element], ignore_index=True)

df_col_text_.to_csv('user_ratings.csv', mode='a', header=False, index=False)

