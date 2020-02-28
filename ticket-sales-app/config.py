import sqlite3

conn = sqlite3.connect("tickets.db")

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')


c.execute('''INSERT INTO stocks VALUES
             ('2020-01-01', 'a', 'b', 0, 1)''')

c.execute("SELECT * FROM stocks WHERE trans = 'a'")
rows = c.fetchall()
print(rows)


# CREATE TABLE BANDS(
# ID INT NOT NULL IDENTITY(1,1),
# NAME VARCHAR (100),
# CATEGORY VARCHAR (100),
# CONSTRAINT PK_BANDS PRIMARY KEY (ID)
# );
# CREATE TABLE CONCERTS (
# ID INT NOT NULL IDENTITY(1,1),
# BANDS_ID INT NOT NULL,
# LOCAL VARCHAR (250),
# DATE DATETIME,
# TICKETS_AVAILABLE,
# CONSTRAINT PK_CONCERTS PRIMARY KEY (ID)
# CONSTRAINT FK_BANDS_ID FOREIGN KEY (BANDS_ID) RE
