# Movie API

El proyecto consiste en una API desarrollada en Flask que permite interactuar con una base de datos de películas. La API ofrece funcionalidades para obtener una lista de películas y para crear nuevas entradas de películas en la base de datos. Utiliza SQLAlchemy como ORM para interactuar con la base de datos y Marshmallow para la serialización de los objetos de película.

La estructura del proyecto incluye:

-   **Modelos**: Definidos en models/movie.py, donde Movie es el modelo de datos para las películas y MovieSchema es el esquema utilizado para serializar y deserializar instancias del modelo.
-   **Rutas**: En routes/movies.py, se definen las rutas de la API para obtener y crear películas. Estas rutas utilizan los servicios definidos para interactuar con la base de datos.
-   **Servicios**: En services/movie.py, se implementan los métodos para obtener todas las películas y para crear una nueva película, interactuando directamente con la base de datos a través de SQLAlchemy.
-   **Configuración de la aplicación**: En app.py, se configura la aplicación Flask, incluyendo la conexión a la base de datos y el registro de las rutas.

La API está configurada para permitir solicitudes CORS, facilitando así su consumo desde aplicaciones en dominios diferentes. Además, se utiliza un esquema de base de datos MySQL para el almacenamiento de los datos.

## Endpoints

---

#### Crear peicula

<details>
 <summary><code>POST</code> <code><b>/movies</b></code> <code>Crea una nueva pelicula</code></summary>

##### Parameters

> | name     | type     | data type | description                       |
> | -------- | -------- | --------- | --------------------------------- |
> | title    | required | string    | Nombre de la película             |
> | overview | required | string    | Descripción de la película        |
> | rating   | required | float     | Calificación de la película       |
> | year     | required | string    | Año de lanzamiento de la pelicula |
> | image    | required | string    | URL poster de la película         |

</details>

#### Listar pelicuas

<details>
 <summary><code>GET</code> <code><b>/movies</b></code> <code>Obtener listado de peliculas</code></summary>

##### Parameters

> | name | type | data type | description |
> | ---- | ---- | --------- | ----------- |
> | None | N/A  | N/A       | N/A         |

</details>

---
