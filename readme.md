#  Microservicio de Facturas (Python y Flask)

Microservicio simple en **Python + Flask** para **crear** y **consultar** facturas.
Ideal para aprender los conceptos básicos de APIs REST y microservicios.

![Microservicio de Facturas (Python y Flask)](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/refs/heads/master/microservicio-facturas-python-flask-1.png)

![Microservicio de Facturas (Python y Flask)](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/refs/heads/master/microservicio-facturas-python-flask-2.png)

## Características del Microservicio

* API mínima con endpoints `POST` y `GET`.
* IDs únicos generados con `UUID` (sin contadores globales).
* Almacenamiento temporal en memoria (ideal para pruebas o POC).
* Código limpio, simple y bien documentado.


### **Instalar dependencias**

```bash
pip install -r requirements.txt
```

## Endpoints disponibles

### POST `/facturas`
Crea una nueva factura

**Cuerpo JSON:**

```json
{
  "cliente": "Urian",
  "total": 120000
}
```

**Respuesta 201:**
```json
{
  "id": "8f45b9f17a33495f8b4cb9c88b9c42e1",
  "cliente": "Urian",
  "total": 120000
}
```

**Errores posibles:**
* `400 Bad Request` → Datos incompletos.

### GET `/facturas/<id>`
Consulta una factura por su ID

**Ejemplo:**

```bash
curl http://127.0.0.1:5000/facturas/8f45b9f17a33495f8b4cb9c88b9c42e1
```

**Respuesta 200:**

```json
{
  "id": "8f45b9f17a33495f8b4cb9c88b9c42e1",
  "cliente": "Urian",
  "total": 120000
}
```

**Errores posibles:**

* `404 Not Found` → Factura no encontrada.


## Notas

* Los datos se almacenan **en memoria**, por lo que **se pierden al reiniciar** el servidor.
* En producción se recomienda:

  * Usar una base de datos (PostgreSQL, MySQL, MongoDB, etc.)
  * Manejar errores y logs adecuadamente.
  * Añadir autenticación o control de acceso.


#### `Flask`

Es la **clase principal** del framework Flask.
Con ella creas la aplicación web o API.

```python
from flask import Flask

app = Flask(__name__)
```
Esto crea una instancia del servidor web que manejará tus rutas (endpoints).

####  `request`
Sirve para **leer los datos que el cliente envía** al servidor.
Por ejemplo, en un `POST` donde mandas un JSON con los datos de una factura:

```python
from flask import request

# get_json() es un método del objeto request en Flask.
# Lee el cuerpo del request como JSON y lo convierte en un diccionario Python.
data = request.get_json()
print(data)
# {"cliente": "Urian", "total": 120000}
```
`request` Es un objeto global de Flask que representa la petición HTTP que llegó al servidor. Te deja acceder al cuerpo (`body`), cabeceras (`headers`), método (`method`), y parámetros (`args`) del request. 

`.get_json()` → es un método que lee el cuerpo (`body`) de esa petición y lo convierte automáticamente a un diccionario de Python, si el contenido es `JSON` válido.

#### `jsonify`
Convierte tus **respuestas Python en JSON** de forma automática y segura.

```python
from flask import jsonify

# Ejemplo de uso
return jsonify({"mensaje": "Factura creada con éxito"})
```