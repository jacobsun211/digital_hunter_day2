def query1_to_dict(data):
    response = []
    for row in data:
        to_dict = {"entity_id": row[0],
                   "target_name":row[1],
                   "priority_level": row[2],
                   "movement_distance_km": row[3]}

        response.append(to_dict)
    return response

    
def query2_to_dict(data):
    response = []
    for row in data:
        to_dict = {"signal_type": row[0],
                   "number_of_reports":row[1]}
        response.append(to_dict)
    return response
    
def query3_to_dict(data):
    response = []
    for row in data:
        to_dict = {"entity_id": row[0],
                   "number_of_reports":row[1]}
        response.append(to_dict)
    return response

def qury4_to_dict(data):
    response = []
    for row in data:
        to_dict = {"entity_id": row[0]}
        response.append(to_dict)
    return response

def qury6_to_dict(data):
    response = []
    for row in data:
        to_dict = {"entity_id": row[0],
                   "target_name":row[1],
                   "priority_level": row[2],
                   "movement_distance_km": row[3]}
        response.append(to_dict)
    return response