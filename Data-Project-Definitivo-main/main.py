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

#Copiamos url para descargar el json barrios

URL= 'https://valencia.opendatasoft.com/explore/dataset/barris-barrios/download/?format=json&timezone=Europe/Berlin&lang=es'

#Obtenemos json barrios y transformamos a datafarme

respuesta = requests.get(url=URL)

datos_barrios=respuesta.json()

df_barrios = pd.json_normalize(datos_barrios)

#Copiamos url para descargar el json Transporte

URL= 'https://valencia.opendatasoft.com/explore/dataset/transporte-barrios/download/?format=json&timezone=Europe/Madrid&lang=es'

#Obtenemos json Transporte y transformamos a datafarme

respuesta = requests.get(url=URL)

datos_transporte=respuesta.json()

df_transporte = pd.json_normalize(datos_transporte)

#LEER CSV SUPERFICIE

df_superficie = pd.read_csv('Superficie.csv', sep=';')
print(df_superficie)

#CONEXION A POSTGREESQL

connection = psycopg2.connect(user="postgres", password="Welcome01",host="postgres", port="5432", database="postgres")
cursor = connection.cursor()

#Crear tabla hospitales

cursor.execute(
  """
    CREATE TABLE IF NOT EXISTS hospitales(
    nombre varchar(50),
    coddistrit varchar(50),
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

#Crear tabla Transporte
cursor.execute(
  """
    CREATE TABLE IF NOT EXISTS Transporte(
    nombre varchar(50),
    coddistrit varchar(50));
    
  """
) 

#Crear tabla Superficie
cursor.execute(
  """
    CREATE TABLE IF NOT EXISTS Superficie(
    coddistrit varchar(50),
    superficie float);
    
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

#Insertar datos en tabla Transporte
for i in range(len(df_transporte)):  

  postgres_insert_query = """ INSERT INTO Transporte (nombre,coddistrit) VALUES (%s,%s)"""
  record_to_insert1 = (df_transporte['fields.nombre'][i],df_transporte['fields.coddistrit'][i])
  cursor.execute(postgres_insert_query, record_to_insert1)

#Insertar datos en tabla Transporte
for i in range(len(df_superficie)):
  postgres_insert_query = """ INSERT INTO Superficie (coddistrit,superficie) VALUES (%s,%s)"""
  record_to_insert1 = (str(df_superficie.iloc[i]['Coddistrit'])[:-2],df_superficie.iloc[i]['Superficie'])
  cursor.execute(postgres_insert_query, record_to_insert1)
connection.commit()