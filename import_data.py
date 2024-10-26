import sqlite3
import requests

def fetch_data():
    api_url = "https://api.artic.edu/api/v1/artworks?limit=10"  # 示例URL，可以设置更高的limit
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()['data']
    else:
        print("无法从 API 获取数据")
        return []

def insert_data(artworks):
    conn = sqlite3.connect('artworks.db')
    cursor = conn.cursor()

    for artwork in artworks:
        # 从 API 数据中提取相关信息
        title = artwork.get('title', 'Unknown Title')
        artist = artwork.get('artist_display', 'Unknown Artist')
        year = artwork.get('date_start', None)
        image_id = artwork.get('image_id', '')
        image_url = f"https://www.artic.edu/iiif/2/{image_id}/full/843,/0/default.jpg" if image_id else None
        description = artwork.get('thumbnail', {}).get('alt_text', 'No Description')

        # 将数据插入到数据库中
        cursor.execute('''
            INSERT INTO artworks (title, artist, year, image_url, description)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, artist, year, image_url, description))

    conn.commit()
    conn.close()
    print("数据导入成功")

if __name__ == '__main__':
    artworks = fetch_data()
    if artworks:
        insert_data(artworks)
