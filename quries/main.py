from fastapi import FastAPI
from quries.dal import movment_calc_of_priority_targets, query2, query3, query4,query5,query6,query7


app = FastAPI()



@app.get('/1')
def movement_of_priority_targets():
    response = movment_calc_of_priority_targets()
    return {"number of results:":len(response), "results":response}


@app.get('/2')
def que2():
    response = query2()
    return {"number of results:":len(response), "results":response}

@app.get('/3')
def que3():
    response = query3()
    return {"number of results:":len(response), "results":response}

@app.get('/4')
def que4():
    response = query4()
    return {"number of results:":len(response), "results":response}

@app.get('/5')
def que5():
    response = query5()
    return {"number of results:":len(response), "results":response}

@app.get('/6')
def que6():
    response = query6()
    return {"number of results:":len(response), "results":response}

@app.get('/7')
def que7():
    response = query7()
    return {"number of results:":len(response), "results":response}


# uvicorn quries.main:app --reload