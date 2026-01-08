# Proyecto-Final-Qualentum

## Como empezar a desarrollar

En este repositorio encontraremos dos Dockerfile y un docker-compose, los cuales cumplen propositos muy distintos.

- Dockerfile : El Dockerfile de nuestro entorno de desarrollo. Contiene los requisitos minimos para ejecutar y realizar pruebas sobre el software.
- Dockerfile.prod : Nuestro Dockerfile de producción. Se encarga de crear una imagen ligera y desplegable de nuestro software.
- docker-compose.yaml: El docker-compose que usaremos para desplegar el entorno de desarrollo, con base de datos y app.

Lo primero que tendrás que realizar será crear el entorno con el comando:

docker-compose up -d

Una vez se descarguen las imagenes, solo tendras que ejecutar el siguiente comando para acceder:

docker-compose exec develop bash

Dentro del container, podrás ejecutar el programa con run.py.

## Como ejecutar las pruebas

Dentro del container de desarrollo, ejecuta el siguiente comando para iniciar los tests unitarios:

pytest --cov=app

## Como crear nuevas pruebas

Todos los tests se crearán con pytest en el directorio tests/.

## Normas de colaboración en equipo

Para mantener un control sobre el codigo del repositorio, cualquier funcionalidad nueva debera de crearse en una rama aparte llamada feature-[nombre].
Una vez has concluido el desarrollo, deberas de asegurarte de que pasa todos los tests antes de crear tu PR.
Tras una code review, si el codigo es apto, se mergeara con la rama master.