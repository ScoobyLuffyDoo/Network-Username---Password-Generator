from fastapi import FastAPI
import UsernamePassword as UP


app = FastAPI()

# Root Path
@app.get('/password/{passwordLength}')
def root(passwordLength: int):
    return(UP.Generator.get_password(passwordLength))


#running the app uvicorn index:app --reload