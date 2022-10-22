import petl as etl
import pandas as pd

class ETL:

    def __init__(self):
        return

    def read(path: str=None):
        if path != None:
            with open(path,'r') as file:                            
                return file.read()
        return """<!DOCTYPE html><html>
                    <head>
                        <title>ERROR!!!</title>
                    </head>
                    <body>
                        <h1>Ya reprobaste la materia!!</h1>
                        <p>read</p>
                    </body>
                    </html>"""                    
