import sqlite3

conn = sqlite3.connect("tickets.db")

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS bands
             (
             ID INT NOT NULL,
             NAME VARCHAR (100),
             CATEGORY VARCHAR (100),
             CONSTRAINT PK_BANDS PRIMARY KEY (ID)
             )''')


c.execute('''CREATE TABLE IF NOT EXISTS concerts
             (
             ID INT NOT NULL,
             BANDS_ID INT NOT NULL,
             LOCAL VARCHAR (250),
             DATE DATETIME,
             TICKETS_AVAILABLE,
             CONSTRAINT PK_CONCERTS PRIMARY KEY (ID)
             CONSTRAINT FK_BANDS_ID FOREIGN KEY (BANDS_ID) REFERENCES BANDS(ID)
             )''')


#
# c.execute('''INSERT INTO bands VALUES
#              ('2020-01-01', 'a', 'b', 0, 1)''')
#
c.execute("SELECT * FROM bands")
rows = c.fetchall()
print(rows)
