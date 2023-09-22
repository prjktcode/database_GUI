import sqlite3

conn = sqlite3.connect('database-3nf.db')

conn_new = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = OFF")

cursor_new = conn_new.cursor()

cursor.execute("SELECT * FROM features_data_set")
data = cursor.fetchall()

cursor.execute("SELECT DISTINCT Dept FROM sales_data_set")
data = cursor.fetchall()

for row in data:
    cursor_new.execute("INSERT INTO depts (dept_name) VALUES (?)", (row[0],))

try:
    for row in data:
        cursor_new.execute("INSERT INTO features (store_id, date, temperature, fuel_price, markdown1, markdown2, markdown3, markdown4, markdown5, cpi, unemployment, is_holiday) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12]))
except:
    pass

cursor.execute("SELECT * FROM sales_data_set")
data = cursor.fetchall()

try:
    for row in data:
        cursor_new.execute("INSERT INTO sales (store_id, dept_id, date, weekly_sales, is_holiday) VALUES (?,?,?,?,?)", (row[1], row[2], row[3], row[4], row[5]))
except:
    pass
cursor.execute("SELECT * FROM stores_data_set")
data = cursor.fetchall()

try:
    for row in data:
        cursor_new.execute("INSERT INTO stores (store_id, store_type, store_size) VALUES (?,?,?)", (row[1], row[2], row[3]))
except:
    pass

cursor.execute("SELECT * FROM store_info")
data = cursor.fetchall()

try:
    for row in data:
        cursor_new.execute("INSERT INTO managers (store_id, manager_name, years_as_manager, email, address) VALUES (?,?,?,?,?)", (row[1], row[2], row[3], row[4], row[5]))

except:
    pass 
cursor.execute("PRAGMA foreign_keys = ON")

conn_new.commit()

cursor.close()
cursor_new.close()
conn.close()
conn_new.close()