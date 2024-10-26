import sqlite3

def create_database():
    # 连接 SQLite 数据库（如果数据库不存在则创建）
    conn = sqlite3.connect('artworks.db')
    cursor = conn.cursor()

    # 创建艺术作品表结构
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS artworks (
            id INTEGER PRIMARY KEY,
            title TEXT,
            artist TEXT,
            year INTEGER,
            image_url TEXT,
            description TEXT
        )
    ''')

    conn.commit()
    conn.close()
    print("数据库和表结构创建成功")

if __name__ == '__main__':
    create_database()
