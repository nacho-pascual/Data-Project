import requests
import csv
import psycopg2


URL= 'https://valencia.opendatasoft.com/api/records/1.0/search/?dataset=hospitales&q=&facet=nombre&facet=financiaci&facet=tipo&facet=fecha&facet=barrio'
  
#Obtenemos el paquete/caja que nos viene de ahi con el get'
respuesta = requests.get(url=URL)

datos=respuesta.json()
print(datos)
  
with open('hospitales.csv', 'a', newline='') as h: 
      writer=csv.DictWriter(h,datos)
      writer.writerow(datos)

#CONEXION A POSTGREESQL
conn = psycopg2.connect(database='postgres',host='postgres',user='postgres',password='Welcome01')
cur = conn.cursor()
cur.execute(
  """
    CREATE TABLE IF NOT EXISTS hospitales(
    geo_point_2d polygon,
    geo_shape polygon,
    Nombre  text ,
    Financiaci  text ,
    Tipo  text ,
    Camas int,
    Direccion  text ,
    Fecha text,
    Barrio text PRIMARY KEY,
    codbarrio text,
    coddistbar text,
    coddistrit text,
    x float,
    y float
)
""")


#This is how we use copy_from() to load our file instead of looping INSERT commands:

with open('hospitales.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f) # Skip the header row.
    cur.copy_from(f, 'hospitales', sep=',')



conn.commit()