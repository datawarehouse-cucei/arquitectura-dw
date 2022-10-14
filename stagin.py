import petl as etl
import psycopg2
import os
conexion = psycopg2.connect(database="inegi", 
                            user="postgres", password="postgres",
                            host="localhost", port="5432")

tbl_inegi2010 = etl.fromxlsx('INEGI/INEGI_2010.xlsx',sheet='hoja')

print("INEGI_2010\n",tbl_inegi2010)

tbl_headers_inegi_2010 = etl.header(tbl_inegi2010)

print("Headers, INEGI_2010\n",tbl_headers_inegi_2010)

tbl_headers_inegi_2010 = tbl_headers_inegi_2010[2:]

print("INEGI_2010, after cut\n",tbl_headers_inegi_2010)

tbl_inegi2010 = etl.cut(tbl_inegi2010,tbl_headers_inegi_2010)

print(tbl_inegi2010)

tbl_inegi2010 = etl.skip(tbl_inegi2010,2)

print(tbl_inegi2010)

tbl_inegi2011 = etl.fromxlsx('INEGI/INEGI_2011.xlsx',sheet='hoja')
tbl_headers_inegi_2011 = etl.header(tbl_inegi2011)
tbl_headers_inegi_2011 = tbl_headers_inegi_2011[2:]
tbl_inegi2011 = etl.cut(tbl_inegi2011,tbl_headers_inegi_2011)

tbl_inegi_union = etl.cat(tbl_inegi2010,tbl_inegi2011)

print("UNION INEGI_2010, INEGI_2011\n",tbl_inegi_union)

#Si es posible cambiar el formato de los archivos y eliminar algunas columnas, si no hacer manualmente

#Para cada archivo INEGI, eliminar la primera columna y unir todos en una sola tabla

#Crear tabla y mandar a la base de datos
#Crear tabla vehiculos en base de datos inegi
#insertar datos de archivo 'ParqueVehicular.xlsx'

#Para los archivos RAMA

#Crear una base de datos RAMA

#Crear tablas CO, NO, NO2, NOX, O3, PM10, PM25, SO2

#Leer archivos CO y unir con el resto de años.

#Insertar en tabla RAMA.CO

#Hacer lo mismo con el resto de archvos, NO, NO2, NOX, O3, PM10, PM25, SO2