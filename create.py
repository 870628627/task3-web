import sqlite3
# Creates file "example.db" if necessary
connection = sqlite3.connect('task3/db.sqlite')
cursor = connection.cursor()


# SQL statement to create a table
cursor.execute('''
CREATE TABLE Clients (
    ID INT PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT,
    Title TEXT,
    Country TEXT,
    Address TEXT,
    Is_Royal BOOLEAN

)
''')

# Create Artworks table
cursor.execute('''
CREATE TABLE Artworks (
    ID INTEGER PRIMARY KEY,
    Title TEXT,
    Artist TEXT,
    Year INT
)
''')

# Create Purchases table
cursor.execute('''
CREATE TABLE IF Purchases (
    ID INT PRIMARY KEY,
    Client_ID INT REFERENCES Clients(Client_ID),
    Artwork_ID INT REFERENCES Artworks(Artwork_ID),
    Price REAL,
    Date TEXT
)
''')

# Commit changes and close the connection
connection.commit()
connection.close()

print("Database and tables created successfully.")
