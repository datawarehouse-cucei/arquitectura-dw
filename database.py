from dotenv import dotenv_values
import psycopg2 

config = dotenv_values('.env')

def set_conexion(db: str=config['DATABASE'], port:str=config['PORT'],
                 user:str=config['PASSWORD'],password:str=config['PASSWORD'], host:str=config['HOST']):
    conexion = psycopg2.connect(database=db, user=user, password=password, host=host, port=port)
    return conexion

def table_exist(table:str,conexion):
    cur = conexion.cursor()
    cur.execute(f"select * from information_schema.tables where table_name='{table}'")
    return bool(cur.rowcount)
