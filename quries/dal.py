import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="digital_hunter",
    user="root",
    password="root"
)
cursor = db.cursor()


def movment_calc_of_priority_targets():
    query = """ 
                SELECT entity_id ,target_name, priority_level, movement_distance_km
                FROM targets 
                WHERE priority_level BETWEEN 1 AND 2 AND movement_distance_km > 5.0
            """
    cursor.execute(query)
    rows = cursor.fetchall()
    response = []
    for row in rows:
        in_dict = {"entity_id": row[0],"target_name":row[1],"priority_level": row[2],"movement_distance_km": row[3] }

        response.append(in_dict)
        print(row)

    return response

def query2():
    query = """ SELECT signal_type, COUNT(*) AS number_of_reports
                FROM intel_signals 
                GROUP BY signal_type
                ORDER BY COUNT(*) DESC"""
    cursor.execute(query)

    rows = cursor.fetchall()
    response = []
    for row in rows:
        response.append(row)
        print(row)

    db.commit()
    return response

def query3():
    query = """ SELECT entity_id, COUNT(*) AS number_of_reports
                FROM intel_signals 
                WHERE entity_id LIKE "TGT-UNKNOWN-%"
                GROUP BY entity_id 
                ORDER BY COUNT(*) DESC
                LIMIT 3"""
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