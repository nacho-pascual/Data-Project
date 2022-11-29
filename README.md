<p align="center">
<img src= "https://datos.gob.es/sites/default/files/styles/success_image/public/success/images/idealista.jpg?itok=uX21SrOq" width="500">
</p>

# Data Project Idealista

El portal líder de compra de vivienda en España, quiere sacar un piloto de calidad de vida aplicado a la vivienda y ha elegido Valencia como sede para su piloto.
La idea de este piloto es ofrecer un mapa de calidad de la vivienda en función de indicadores de datos abiertos.
La calidad de la vivienda se medirá por ruido, hospitales, contaminación... teniendo que valorar la zona en base a dichos parámetros.

### **Contenido del Ejercicio**:

1.  ```DockerFile```: reune los datos con los que vamos a construir la imagen de python .
2.  ```Main.py```: contiene el script de Python que ejecuta el código.
3. ```Requerimientos.txt```: contiene las librerias que le faltan al contenedor para ejecutar el código del script de pyhon.
4. ```DockerCompose```: contiene el código para levantar los 3 contenedores necesarios.
5. ```superficie.csv```: contiene las superficies por distrito de valencia para darte realismo a la visualización de datos.
6. ```links.csv```: contiene los links a idealista que ligaremos a nuestro proyecto de visualizacion.


### **Pasos a seguir para la realización del :**


  1. Construir nuestra imagen de python:
  
    ```docker compose build```
    
  2. Poner en marcha el docker compose con los 3 contenedores:
  
    ```docker compose up```
  3. Video de la solucion:
  
  4. Accedemos al tableu desktop donde nos conectariamos a nuestra base de datos que acabamos de levantar y procederíamos a realizar la visualizacion. 
     Para poder visualizarlo correctamente con la modificación que hemos realizado , hemos cargado la visualización en :
