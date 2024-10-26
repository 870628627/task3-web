import sqlite3

def query_database(keyword=None):
    conn = sqlite3.connect('artworks.db')
    cursor = conn.cursor()

    # 查询包含关键词的艺术作品（按标题或作者）
    if keyword:
        query = '''
            SELECT title, artist, year, image_url, description
            FROM artworks
            WHERE title LIKE ? OR artist LIKE ?
        '''
        cursor.execute(query, (f'%{keyword}%', f'%{keyword}%'))
    else:
        # 没有关键词则返回所有艺术作品
        query = 'SELECT title, artist, year, image_url, description FROM artworks'
        cursor.execute(query)

    # 打印查询结果
    rows = cursor.fetchall()
    for row in rows:
        title, artist, year, image_url, description = row
        print(f"Title: {title}\nArtist: {artist}\nYear: {year}\nImage URL: {image_url}\nDescription: {description}\n")

    conn.close()

if __name__ == '__main__':
    keyword = input("Enter a keyword to search for artworks (leave empty to display all): ")
    query_database(keyword)
# TODO
