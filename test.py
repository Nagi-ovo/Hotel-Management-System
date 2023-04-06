import sqlite3

con = sqlite3.Connection('hm_proj.db')
cur = con.cursor()

cur.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='hoteld';")
print(cur.fetchone()[0])

cur.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='roomd';")
print(cur.fetchone()[0])


cur.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='paymentsf';")
print(cur.fetchone()[0])


cur.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='payments';")
print(cur.fetchone()[0])


con.close()
