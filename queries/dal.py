import mysql.connector
from queries.response_builder import query1_to_dict, query2_to_dict, query3_to_dict, qury4_to_dict
from maps_data.DigitalHunter_map import plot_map_with_geometry

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
    data = cursor.fetchall()
    response = query1_to_dict(data)
    return response

def count_by_signal_type():
    query = """ SELECT signal_type, COUNT(*) AS number_of_reports
                FROM intel_signals 
                GROUP BY signal_type
                ORDER BY COUNT(*) DESC"""
    cursor.execute(query)

    data = cursor.fetchall()
    response = query2_to_dict(data)
    return response

def identify_possible_targets():
    query = """ 
                SELECT entity_id, COUNT(*) AS number_of_reports
                FROM intel_signals 
                WHERE entity_id LIKE "TGT-UNKNOWN-%" OR priority_level = 99 
                GROUP BY entity_id 
                ORDER BY COUNT(*) DESC
                LIMIT 3
            """
    cursor.execute(query)

    data = cursor.fetchall()
    response = query3_to_dict(data)
    return response

def query4():
    query = """ 
                SELECT entity_id
                FROM intel_signals
                WHERE EXTRACT(HOUR FROM created_at) BETWEEN 8 AND 19 
                GROUP BY entity_id
                HAVING MAX(distance_from_last) = 0
            """
    cursor.execute(query)

    rows = cursor.fetchall()
    response = []
    for row in rows:
        response.append(row)
        print(row)

    db.commit()
    return response

def query5(entity):
    inital_points = """
                    SELECT initial_lat , initial_lon  
                    FROM targets 
                    WHERE entity_id = %s
                    """
    last_knowen_points = """
                    SELECT last_known_lat , last_known_lon  
                    FROM targets 
                    WHERE entity_id = %s
                    """
    cursor.execute(inital_points, [entity]) # becouse matplotlib function expects somthing like this: [(35.0, 32.0), (35.2, 32.5)]
    inital_points = cursor.fetchone()

    cursor.execute(last_knowen_points, [entity])
    last_knowen_points = cursor.fetchone()

    points = [inital_points, last_knowen_points]
    plot_map_with_geometry(points) 
    return points

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




# python -m quries.dal

