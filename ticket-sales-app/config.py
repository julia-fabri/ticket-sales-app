import sqlite3

conn = sqlite3.connect("tickets.db")

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS bands
             (
             ID INTEGER PRIMARY KEY AUTOINCREMENT,
             NAME VARCHAR (100),
             CATEGORY VARCHAR (100)
             )''')


c.execute('''CREATE TABLE IF NOT EXISTS concerts
             (
             ID INTEGER PRIMARY KEY AUTOINCREMENT,
             BANDS_ID INT NOT NULL,
             LOCAL VARCHAR (250),
             TICKETS_AVAILABLE INT,
             TIME time,
             DATE DATE,
             CONSTRAINT FK_BANDS_ID FOREIGN KEY (BANDS_ID) REFERENCES BANDS(ID)
             )''')

# c.execute('''INSERT INTO bands VALUES
#              ('2020-01-01', 'a', 'b', 0, 1)''')

c.execute("SELECT * FROM bands")
rows = c.fetchall()
print(rows)
