from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return{'result': "password Generator"}




if __name__ =="__main__":
     main()    


#running the app uvicorn main:app --reload