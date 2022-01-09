from pyvi import ViTokenizer, ViPosTagger
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"res": "Homepage"}


@app.get("/tokenize/{sentence}")
def read_item(sentence: str):
    res = ViPosTagger.postagging(ViTokenizer.tokenize(sentence))
    return {"res": res}