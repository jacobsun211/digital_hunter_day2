import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="digital_hunter",
    user="root",
    password="root"
)
cursor = db.cursor()


def query1():
    query = """SELECT * FROM attacks LIMIT 5"""
    cursor.execute(query)

    rows = cursor.fetchall()
    response = []
    for row in rows:
        response.append(row)
        print(row)

    db.commit()
    return response

def query2():
    query = """SELECT * FROM attacks LIMIT 5"""
    cursor.execute(query)

    rows = cursor.fetchall()
    response = []
    for row in rows:
        response.append(row)
        print(row)

    db.commit()
    return response

def query3():
    query = """SELECT * FROM attacks LIMIT 5"""
    cursor.execute(query)

    rows = cursor.fetchall()
    response = []
    for row in rows:
        response.append(row)
        print(row)

    db.commit()
    return response

def query4():
    query = """SELECT * FROM attacks LIMIT 5"""
    cursor.execute(query)

    rows = cursor.fetchall()
    response = []
    for row in rows:
        response.append(row)
        print(row)

    db.commit()
    return response

def query5():
    query = """SELECT * FROM attacks LIMIT 5"""
    cursor.execute(query)

    rows = cursor.fetchall()
    response = []
    for row in rows:
        response.append(row)
        print(row)

    db.commit()
    return response

def query6():
    query = """SELECT * FROM attacks LIMIT 5"""
    cursor.execute(query)

    rows = cursor.fetchall()
    response = []
    for row in rows:
        response.append(row)
        print(row)

    db.commit()
    return response

def query7():
    query = """SELECT * FROM attacks LIMIT 5"""
    cursor.execute(query)

    rows = cursor.fetchall()
    response = []
    for row in rows:
        response.append(row)
        print(row)

    db.commit()
    return response


# python -m quries.dal

# cursor.close()
# db.close()