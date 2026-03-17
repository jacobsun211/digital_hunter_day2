from fastapi import FastAPI
from queries.dal import movment_calc_of_priority_targets, count_by_signal_type, identify_possible_targets, query4, query5, query6


app = FastAPI()



@app.get('/1')
def movement_of_priority_targets():
    response = movment_calc_of_priority_targets()
    return {"number of results:":len(response), "results":response}


@app.get('/2')
def count_of_signal_type():
    response = count_by_signal_type()
    return {"number of results:":len(response), "results":response}

@app.get('/3')
def identify_possible_new_targets():
    response = identify_possible_targets()
    return {"number of results:":len(response), "results":response}

@app.get('/4')
def que4():
    response = query4()
    return {"number of results:":len(response), "results":response}

@app.post('/5')
def que5(entity: str):
    response = query5(entity)
    return {"number of results:":len(response), "results":response}

@app.get('/6')
def que6():
    response = query6()
    return {"number of results:":len(response), "results":response}




# uvicorn queries.main:app --reload