import sqlite3


conn = sqlite3.connect('hm_proj.db')


conn.execute('''
CREATE FUNCTION get_total_amt() RETURNS NUMBER AS
BEGIN
  DECLARE total NUMBER;
  SELECT SUM(totalamt) INTO total FROM paymentsf;
  RETURN total;
END;
''')


conn.execute('''
CREATE PROCEDURE insert_payment(
  IN f_name VARCHAR,
  IN l_name VARCHAR,
  IN c_number VARCHAR,
  IN email VARCHAR,
  IN r_n NUMBER,
  IN day VARCHAR,
  IN month VARCHAR,
  IN year VARCHAR,
  IN time VARCHAR,
  IN method VARCHAR,
  IN totalamt VARCHAR
)
BEGIN
  INSERT INTO paymentsf (f_name, l_name, c_number, email, r_n, day, month, year, time, method, totalamt) 
  VALUES (f_name, l_name, c_number, email, r_n, day, month, year, time, method, totalamt);
END;
''')


cursor = conn.cursor()
cursor.execute('SELECT get_total_amt()')
print(cursor.fetchone()[0])

cursor.execute('CALL insert_payment("John", "Doe", "1234567890", "johndoe@example.com", 1, "01", "01", "2022", "12:00", "cash", "100")')
conn.commit()


conn.close()
