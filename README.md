# ENTREGA BLACKLIST API

📄 Esta carpeta contiene el código fuente para blacklist API. El proyecto fue realizado utilizando [Python](https://www.python.org/downloads/) versión 3.12


## Contenidos

- [Blacklist API](#blacklist-api)
  - [Contenidos](#contenidos)
  - [Prerrequisitos](#prerrequisitos)
  - [Estructura del proyecto](#estructura-del-proyecto)
  - [Instalación](#instalación)
  - [Ejecución local](#ejecución-local) 
  - [Ejecución Docker](#ejecución-docker)
  - [License](#license)

## Prerrequisitos

Para levantar este proyecto necesitarás:

* [Python](https://www.python.org/downloads/) (con virtualenv)
* Docker.
* Copia local de este repositorio.


## Estructura del proyecto

```
📦 Blaclist API
├── 📁 MISW4304-Proyecto-Devops
│   ├── 📁 entrega
│   │   ├── 📁 db   # Clases para conexión a base de datos.
│   │   ├── 📁 models   # Modelos para base de datos.
│   │   ├── 📁 routers  # Definición de rutas y endpoints.
│   │   ├── 📁 schemas  # Definición de request y responses.
│   │   ├── 📁 services     # Clases con lógica de negocio.
│   │   ├── 📄 main.py  # Clase principal de la microservicio.
├── 📄 .env   # Archivo con las variables de entorno.
├── 📄 Dockerfile   # Archivo para despliegue con docker.
├── 📄 README.md    # Usted está aquí.
└── 📄 requirements.txt     # Definición de dependencias del microservicio.
```

## Instalación

* Abrir una terminal en la raíz del proyecto y ejecutar los siguientes comandos para instalar `Blacklist API`:

    <details>
    <summary>Linux/MacOS</summary>
    <pre><code> cd MISW4304-Proyecto-Devops
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt</code></pre>
    </details>

    <details>
    <summary>Windows</summary>
    <pre><code> cd posts
    python -m venv .venv
    .\.venv\Scripts\activate
    pip install -r requirements.txt</code></pre>
    </details>
    
## Ejecución local

1. Cree una base de datos en postgres:
   
    **Nota**:  Al crearla, rellene los campos que se encuentran en el archivo .env

    DB_USER=usuario de la base de datos
    DB_PASSWORD=contrasena de la base de datos
    DB_HOST_DOCKER=dejar vacio
    DB_PORT=puerto
    DB_NAME=nombre de la base de datos


2.  Correr el comando siguiente:

    ```
    uvicorn entrega.main:app --reload
    ```

2.  Probar endpoints:

    ```
    http://127.0.0.1:8000/
    ```

## Ejecución Docker

1. Cree una base de datos en postgres:
   
    **Nota**:  Al crearla, rellene los campos que se encuentran en el archivo .env

    DB_USER=usuario de la base de datos
    DB_PASSWORD=contrasena de la base de datos
    DB_HOST_DOCKER=db-blacklist
    DB_PORT=puerto
    DB_NAME=nombre de la base de datos


2.  Correr el comando siguiente:

    ```
    docker-compose up --build -d
    ```

3.  Probar endpoints:

    ```
    http://localhost:8000/
    ```



## License

Copyright © MISW4304 - DevOps: Agilizando el Despliegue Continuo de Aplicaciones - 2025.

