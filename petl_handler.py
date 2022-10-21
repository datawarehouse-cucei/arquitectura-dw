import petl as etl
import pandas as pd

class ETL:

    def __init__(self):
        return

    def read(self,path: str=None):
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

    def readyears(self,folder: str = None, start: int=2010, end: int=2010,type: str="CO"):
        if folder != None:
            tablas = ""
            while start <= end:
                path = "/{folder}/{folder}{start}/{start}{type}".format()
                with open(path,'r') as file:                            
                    tablas += file.read()
                start += 1
            return tablas
        return """<!DOCTYPE html><html>
                    <head>
                        <title>ERROR!!!</title>
                    </head>
                    <body>
                        <h1>Ya reprobaste la materia!!</h1>
                        <p>read</p>
                    </body>
                    </html>"""   