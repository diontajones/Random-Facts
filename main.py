from fastapi import FastAPI
import uvicorn
import random

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.get('/random')
async def get_random():
    rn:int = random.randint(0, 100)
    return {'number': rn, 'limit': 100}

@app.get('/random/{limit}')
async def get_random(limit: int):
    rn: int = random.randint(0, limit)
    return {'number': rn, 'limit': limit}

@app.get("/detroit_facts")
async def get_detroit_fact(index: int = None):
    with open("facts.txt", "r") as file:
        facts = file.readlines()
    if index is not None and index < len(facts):
        return {"fact": facts[index].strip()}
    detroit_fact = random.choice(facts).strip()
    return {"fact": detroit_fact}


@app.post("/add")
async def add_fact(new_fact: str):
    with open("facts.txt", "a") as file:
        file.write(new_fact + "\n")
    return {"message": "Fact added successfully"}



