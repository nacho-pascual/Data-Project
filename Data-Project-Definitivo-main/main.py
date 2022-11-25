import requests
import psycopg2
import pandas as pd
import json 
import psycopg2.extras as extras
import numpy
 
#Copiamos url para descargar el json hospitales

URL= 'https://valencia.opendatasoft.com/explore/dataset/hospitales/download/?format=json&timezone=Europe/Madrid&lang=es'

#Obtenemos json hospitales y transformamos a datafarme

respuesta = requests.get(url=URL)

datos=respuesta.json()

df_hospitales = pd.json_normalize(datos)


#Copiamos url para descargar el json espacios verdes

URL= 'https://valencia.opendatasoft.com/explore/dataset/espais-verds-espacios-verdes/download/?format=json&timezone=Europe/Berlin&lang=es'

#Obtenemos json espacios verdes y transformamos a datafarme

respuesta = requests.get(url=URL)

datos_espaciosverdes=respuesta.json()

df_espacios_verdes = pd.json_normalize(datos_espaciosverdes)

print(df_espacios_verdes)

#Copiamos url para descargar el json barrios

URL= 'https://valencia.opendatasoft.com/explore/dataset/barris-barrios/download/?format=json&timezone=Europe/Berlin&lang=es'

#Obtenemos json barrios y transformamos a datafarme

respuesta = requests.get(url=URL)

datos_barrios=respuesta.json()

df_barrios = pd.json_normalize(datos_barrios)

print(df_barrios)

#Copiamos url para descargar el json cargadores electricos

URL= 'https://valencia.opendatasoft.com/explore/dataset/carregadors-vehicles-electrics-cargadores-vehiculos-electricos/download/?format=json&timezone=Europe/Berlin&lang=es'

#Obtenemos json cargadores electricos y transformamos a datafarme

respuesta = requests.get(url=URL)

datos_cargadores=respuesta.json()

df_cargadores = pd.json_normalize(datos_cargadores)

#CONEXION A POSTGREESQL

connection = psycopg2.connect(user="postgres", password="Welcome01",host="postgres", port="5432", database="postgres")
cursor = connection.cursor()

#Crear tabla hospitales

cursor.execute(
  """
    CREATE TABLE IF NOT EXISTS hospitales(
    nombre varchar(50),
    coddistrit integer,
    x varchar(50),
    y varchar(50));
    
  """
)

#Crear tabla espacios verdes
cursor.execute(
  """
    CREATE TABLE IF NOT EXISTS espaciosverdes(
    nombre varchar(100),
    barrio varchar(50));
    
  """
)

#Crear tabla barrios 
cursor.execute(
  """
    CREATE TABLE IF NOT EXISTS barrios(
    nombre varchar(50),
    barrio varchar(50));
    
  """
)

#Crear tabla cargadores electricos
cursor.execute(
  """
    CREATE TABLE IF NOT EXISTS cargadores(
    datasetid varchar(100),
    distrito integer);
    
  """
)

#Insertar datos en tabla hospitales
for i in range(len(df_hospitales)):  

  postgres_insert_query = """ INSERT INTO hospitales (nombre,coddistrit,x,y) VALUES (%s,%s,%s,%s)"""
  record_to_insert = (df_hospitales['fields.barrio'][i],df_hospitales['fields.coddistrit'][i],df_hospitales['fields.x'][i],df_hospitales['fields.y'][i])
  cursor.execute(postgres_insert_query, record_to_insert)
connection.commit()


#Insertar datos en tabla espacios verdes
for i in range(len(df_espacios_verdes)):  

  postgres_insert_query = """ INSERT INTO espaciosverdes (nombre,barrio) VALUES (%s,%s)"""
  record_to_insert = (df_espacios_verdes['fields.nombre'][i],df_espacios_verdes['fields.barrio'][i])
  cursor.execute(postgres_insert_query, record_to_insert)
connection.commit()

#Insertar datos en tabla barrios
for i in range(len(df_barrios)):  

  postgres_insert_query = """ INSERT INTO barrios (nombre,barrio) VALUES (%s,%s)"""
  record_to_insert1 = (df_barrios['fields.nombre'][i],df_barrios['fields.coddistrit'][i])
  cursor.execute(postgres_insert_query, record_to_insert1)
connection.commit()

#Insertar datos en tabla cargadores electricos
for i in range(len(df_cargadores)):  

  postgres_insert_query = """ INSERT INTO cargadores (datasetid,distrito) VALUES (%s,%s)"""
  record_to_insert = (df_cargadores['datasetid'][i],df_cargadores['fields.distrito'][i])
  cursor.execute(postgres_insert_query, record_to_insert)
connection.commit()