from fastapi import FastAPI, BackgroundTasks
import uvicorn
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    number_1: float
    number_2: float


@app.post("/")
def divide(item: Item, background_tasks: BackgroundTasks):

    # if item.number_1 is not float or item.number_2 is not float:
    #     result = "error"
    if item.number_2 == 0:
        result = "error"
    else:
        result = item.number_1 / item.number_2

    background_tasks.add_task(write_log, item, result)

    return {"result": result}

def write_log(item: Item, result):
    with open("log.txt", "a") as log_file:
        content = f"{item.number_1} / {item.number_2} = {result}"
        log_file.write(content + "\n")

if __name__ == "__main__":
    uvicorn.run(app,host='0.0.0.0', port=8000)