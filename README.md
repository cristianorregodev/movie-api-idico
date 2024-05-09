# Movie API

API básica para consumir datos de peliculas y crear peliculas. Prueba técnica IDICO.

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
