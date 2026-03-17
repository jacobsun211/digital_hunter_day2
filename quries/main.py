from fastapi import FastAPI
from quries.dal import query1


app = FastAPI()



@app.get('/')
def que1():
    response = query1()
    return {"number of results:":len(response), "results":response}


@app.get('/')
def que2():
    response = query1()
    return {"number of results:":len(response), "results":response}

@app.get('/')
def que3():
    response = query1()
    return {"number of results:":len(response), "results":response}

@app.get('/')
def que4():
    response = query1()
    return {"number of results:":len(response), "results":response}

@app.get('/')
def que5():
    response = query1()
    return {"number of results:":len(response), "results":response}

@app.get('/')
def que6():
    response = query1()
    return {"number of results:":len(response), "results":response}

@app.get('/')
def que7():
    response = query1()
    return {"number of results:":len(response), "results":response}


# uvicorn quries.main:app --reload