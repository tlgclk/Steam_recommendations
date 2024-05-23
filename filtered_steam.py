import pandas as pd

# CSV dosyasını oku
df = pd.read_csv('steam.csv')

# Sadece ilgili sütunları seç
df_filtered = df[['appid', 'name', 'median_playtime']]

# median_playtime sütunu 0 olmayan öğeleri filtrele
df_non_zero = df_filtered[df_filtered['median_playtime'] != 0]

# Filtrelenmiş verileri içeren bir sözlük oluştur
filtered_steam_data = {
    'appid': df_non_zero['appid'].tolist(),
    'name': df_non_zero['name'].tolist(),
    'median_playtime': df_non_zero['median_playtime'].tolist()
}

# Filtrelenmiş DataFrame'i yeni bir CSV dosyasına kaydet
df_non_zero.to_csv('filtered_steam.csv', index=False)
