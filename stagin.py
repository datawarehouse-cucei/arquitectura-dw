import petl as etl
import pandas as pd
import psycopg2
import re
import os

#funciones petl utilizadas fromcsv, head, tail, nrows, rowslice, appendcsv, todb, tohtml, tjson, convert

#obtener direciones de la carpeta INEGI -- done

ingei_paths = os.listdir("INEGI/")

#Leer archivos para limpieza y exportar a csv --done

column_headers =  ["Id","C_vehivulo_automotor","C_peaton","C_animal","C_objeto_fijo","Volcadura","Caida_de_pasajero","Salida_del_camino","Incendio","C_ferrocarril","C_motocicleta","C_ciclista","Otro"]
anio = 2010

for path in ingei_paths:
    inegi_tbl = pd.read_excel("INEGI/"+path,skiprows=19,names=column_headers,header=None)
    inegi_tbl.to_csv(f"INEGI/INEGI_{anio}.csv".format(anio))
    anio += 1

#Tomar el path de los archivos csv creado para leerlos con petl -- done
inegi_file = os.listdir("INEGI/")
inegi_csv = []
for path in inegi_file:
    if re.findall(".csv$",path):        
        inegi_csv.append(path)

#Leer archivo y revisar con las últimas filas y eliminar ultimas filas --done
#Unir en un archivo csv

os.mkdir("INEGI/INEGI_JOIN.csv")

for path in inegi_csv:
    tbl_inegi = etl.fromcsv("INEGI/"+path)
    print(etl.head(tbl_inegi,4))
    print(etl.tail(tbl_inegi,4))
    nrows = etl.nrows(tbl_inegi)
    tbl2_inegi = etl.rowslice(tbl_inegi,0,nrows-4)
    etl.appendcsv(tbl2_inegi,"INEGI/INEGI_JOIN.csv")
    print(etl.tail(tbl2_inegi,1))

tbl_inegi_join = etl.fromcsv("INEGI/INEGI_JOIN.csv")

#convierte un valor a flotante
#tbl_inegi_join = etl.convert()
conexion = psycopg2.connect(database="inegi", 
                            user="postgres", password="postgres",
                            host="localhost", port="5432")

etl.todb(tbl_inegi_join, conexion, 'tabla', create=False)
etl.tohtml(tbl_inegi_join, 'tabla.html',caption='Tabla de datos')
etl.tojson(tbl_inegi_join, 'tabla.json')
