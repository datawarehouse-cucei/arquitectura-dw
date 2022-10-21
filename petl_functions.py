from lib2to3.pytree import convert
import petl as etl
import pandas as pd
import re
import os
from database import conexion as conn
from database import table_exist

#funciones utilizadas, etl.setheader, etl.tohtml, etl.tojson, etl.fromxls, etl.fromcsv, etl.rowslice, etl.todb

def to_html(folder: str,type:str):
    paths = get_folder_content(folder,type)
    header = etl.fromcsv(f"{folder}/{paths[0]}")    
    for path in paths:
        if os.path.exists(folder+path):
            table = etl.fromcsv(f"{folder}/{path}")
            table = etl.cut(table,header[0])
            path = os.path.basename(path)
            path = os.path.splitext(path)[0]+".html"
            if os.path.exists(f"{folder}{path}"):
                os.remove(f"{folder}{path}")
            etl.tohtml(table,f"{folder}{path}")

def to_json(folder: str,type:str):
    paths = get_folder_content(folder,type)
    header = etl.fromcsv(f"{folder}/{paths[0]}")    
    for path in paths:
        if os.path.exists(folder+path):
            table = etl.fromcsv(f"{folder}/{path}")
            table = etl.cut(table,header[0])
            path = os.path.basename(path)
            path = os.path.splitext(path)[0]+".json"
            if os.path.exists(f"{folder}{path}"):
                os.remove(f"{folder}{path}")
            etl.tojson(table,f"{folder}{path}")    

def to_db(folder:str, file:str, table:str, conexion, override: bool = True):
    tabla = etl.fromcsv(f"{folder}{file}")
    etl.todb(tabla, conexion, table, create=override)


def get_folder_content(folder: str = None,content_type: str="all"):
    content = []
    if content_type == "all":
        content = os.listdir(f"{folder}")
    else:
        for path in os.listdir(f"{folder}"):
            if re.findall(f".{content_type}$",path):        
                content.append(path)
    return content

def convert_xls_to_csv(folder:str=None,files:list=[]):    
    for path in files:
        table = pd.read_excel(f"{folder}{path}")
        path = os.path.basename(path)
        path = os.path.splitext(path)[0]
        if not os.path.exists(path+".csv"):
            table.to_csv(folder+path+".csv")

def check_rowcount(folder):
    paths = get_folder_content(folder,"csv")    
    for path in paths:
        if os.path.exists(folder+"/"+path):
            table = etl.fromcsv(f"{folder}/{path}")
            print(path)
            print(etl.rowlengths(table))

def remove_column(folder:str=None,index:int=0):
    paths = get_folder_content(folder,"csv")
    for path in paths:
        if os.path.exists(folder+path):
            table = etl.fromcsv(f"{folder}{path}")
            header = etl.header(table)
            table2 = etl.cutout(table,header[index])
            etl.tocsv(table2,f"{folder}c{path}")

def change_headers(table,headers:list=None)->str:
    column_count = len(etl.header(table))
    if len(headers) != column_count:
        return "Header count mismatch"
    table = etl.setheader(table,headers)
    return table

def remove_files(folder:str,exten:str,name=str):
    files = get_folder_content(folder)
    for file in files:
        if file[-3:] == exten and file[0] == name:
            os.remove(folder+file)
