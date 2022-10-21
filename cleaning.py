from petl_functions import *

#convertir .xls en inegi a .csv
INEGI = "INEGI/"
RAMA = "RAMA/"
files = get_folder_content(INEGI,"xls")
convert_xls_to_csv(INEGI,files)

folders = get_folder_content(RAMA)
for folder in folders:
    files = get_folder_content(RAMA+folder+"/","xls")
    convert_xls_to_csv(RAMA+folder+"/",files)

## Limpieza

#   check irregularities filas irregulares

check_rowcount(INEGI)

for folder in folders:
    check_rowcount(RAMA+folder)    

#   quitar primera columna

remove_column(INEGI)

files = get_folder_content(INEGI,"csv")

remove_files(INEGI,"csv","I")

files = get_folder_content(INEGI,"csv")

for file in files:
    newname= file[1:]
    os.rename(INEGI+file,f"{INEGI}{newname}")

to_html(INEGI,"csv")

#   obtener encabezados

for folder in folders:
    to_html(RAMA+folder,"csv")

#   remover primera fila después del encabezadi

to_json(INEGI,"csv")

for folder in folders:
    to_json(RAMA+folder,"csv")

files = get_folder_content(INEGI,"csv")

#Change headers
new_headers = ['index','total','C_V_Auto','C_Peaton','C_Animal','C_Objeto_Fijo','Volcadura','Caida_pasajero','Salida_camino','Incendio','C_Ferrocaril','C_Moto','C_Ciclista','Otro']

for file in files:
    table = etl.fromcsv(INEGI+file)
    table = change_headers(table,new_headers)
    etl.tocsv(table,f"{INEGI}n{file}")

remove_files(INEGI,"csv","I")

files = get_folder_content(INEGI,"csv")

for file in files:
    newname= file[1:]
    os.rename(INEGI+file,f"{INEGI}{newname}")

files = get_folder_content(INEGI,"csv")

for file in files:
    table = os.path.basename(file)
    table = os.path.splitext(file)[0]
    to_db(INEGI, file,f"{table}",conn, not table_exist(table))

RAMA = "RAMA/"

folders = get_folder_content(RAMA)

for folder in folders:
    files = get_folder_content(RAMA+folder)
    for file in files:
        table = os.path.basename(file)
        table = os.path.splitext(file)[0]
        table = "RAMA"+table[4:]
        to_db(f"{RAMA}{folder}/", file,table,conn, not table_exist(table))