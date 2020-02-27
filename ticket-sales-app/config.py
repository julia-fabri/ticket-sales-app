import sqlite3
from concerts import Concerts

conn = sqlite3.connect('teste.db')

c = conn.cursor()

# c.execute("""CREATE TABLE concerts (
#             band_name text,
#             local text,
#               datetime datetime
#         )""")

conc1 = Concerts('Foo Fighters', 'Morumbi', '2020-01-01')
print(conc1.band_name)

# c.execute("INSERT INTO concerts VALUES (?, ?, ?)", (conc1.band_name, conc1.local, conc1.datetime))



c.execute("SELECT * FROM concerts")

print(c.fetchone())

conn.commit()

conn.close()