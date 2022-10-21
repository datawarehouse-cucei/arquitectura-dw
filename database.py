from dotenv import dotenv_values
import psycopg2 

config = dotenv_values('.env')

conexion = psycopg2.connect(database=config['DATABASE'], 
                            user=config['PASSWORD'], password=config['PASSWORD'],
                            host=config['HOST'], port=config['PORT'])

cur = conexion.cursor()

def table_exist(table:str):
    cur.execute(f"select * from information_schema.tables where table_name='{table}'")
    return bool(cur.rowcount)