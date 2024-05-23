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
game_play_median = pd.read_csv('filtered_steam.csv')

def get_df(aa):
    ss = aa.json()
    sd = pd.DataFrame(ss['response']['games'])
    #sd.drop(sd.columns[[1,3, 4, 5]], axis = 1, inplace = True)
    no_zero = sd.loc[sd['playtime_forever']!=0]
#ddf_col = pd.concat([aaaa,game_play_median], axis=1)
    df_col = pd.merge(no_zero, game_play_median, on="appid")
    return df_col

for i in range(8):
    
    df_col_ = get_df(requests.get(df_user_links['Links'][i]))    ###### Anti_crawler when i >= 9
    