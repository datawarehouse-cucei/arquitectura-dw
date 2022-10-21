from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse
from database import db, config
import petl as etl

app = FastAPI()

@app.get("/")
async def main():
    return "Diseño de la arquitectura del almacen de datos"

@app.get("/INEGI",response_class=PlainTextResponse) 
async def get_inegi(from_: str = "2010", to_:str="2010"):
    return "/INEGI/INEGI_"+from_+".csv"

@app.get("/INEGIHTML",response_class=HTMLResponse)
async def get_inegi_html(from_: str = "2010", to_:str="2010"):
    table = etl.fromxls(f"INEGI/INEGI_{from_}")
    table = etl.teehtml(table)
    return table

@app.get("/INEGIJSON",response_class=JSONResponse)
async def get_inegi_json(from_: str = "2010", to_:str="2010"):
    return   

@app.get("/")
async def main():
    return "Diseño de la arquitectura del almacen de datos"

@app.get("/RAMAHTML",response_class=PlainTextResponse)
async def get_rama(from_: str = "2010", to_:str="2010"):
    return 

@app.get("/RAMA",response_class=HTMLResponse)
async def get_rama(from_: str = "2010", to_:str="2010"):
    return 

@app.get("/RAMAJSON",response_class=JSONResponse)
async def get_rama(from_: str = "2010", to_:str="2010"):
    return   
