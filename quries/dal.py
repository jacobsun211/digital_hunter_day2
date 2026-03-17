import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="digital_hunter",
    user="root",
    password="password"
)



cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        role VARCHAR(50)
    )
""")

sql = "INSERT INTO users (name, role) VALUES (%s, %s)"
values = ("Alice", "Admin")

cursor.execute(sql, values)

db.commit()
cursor.close()
db.close()

print("One record inserted successfully!")


# pip install mysql-connector-python --no-cache-dir
