# Importando Flask y otras librerías necesarias
from flask import Flask, request, jsonify
import uuid  # Generación de IDs únicos sin estado global

# Creando la aplicación Flask
app = Flask(__name__)

# Simulamos una "base de datos" en memoria con un diccionario.
facturas = {}

# Endpoint para obtener todas las facturas
@app.route('/facturas', methods=['GET'])
def obtener_facturas():
    """Devuelve todas las facturas almacenadas."""
    return jsonify(facturas)


# Endpoint para crear una factura
@app.route("/facturas", methods=["POST"])
def crear_factura():
    # Obtenemos los datos JSON enviados en la solicitud POST.
    print(f"request.data: {request.data}")
    print(f"request.get_json(): {request.get_json()}")
    
    """
    get_json() es un método del objeto request en Flask.
    Lee el cuerpo del request como JSON y lo convierte en un diccionario Python.
    """
    data = request.get_json()

    """
     Validamos que: Si no hay datos, o si el campo cliente no está en los datos,
     o si el campo total no está en los datos.
    """
    if not data or "cliente" not in data or "total" not in data:
        # Si falta algún campo requerido, retornamos un error.
        return jsonify({"error": "Datos incompletos"}), 400

    # Definimos la factura con los datos recibidos y un ID único, en un diccionario de Python.
    factura = {
        "id": uuid.uuid4().hex,  # ID único en formato hexadecimal
        "cliente": data["cliente"], # Nombre del cliente
        "total": data["total"], # Total de la factura
    }

    # Guarda la factura en la "base de datos" en memoria, dentro del diccionario facturas, usando su ID como clave.
    # En el diccionario facturas, se guarda la factura usando su ID como clave, recordando que un diccionario es una colección de pares clave-valor.
    facturas[factura["id"]] = factura
    # Retornamos la factura creada con un código de estado 201 (Created).
    return jsonify(factura), 201


# Endpoint para consultar una factura por ID
@app.route("/facturas/<factura_id>", methods=["GET"])  # ID es una cadena UUID
def obtener_factura(factura_id):
    """Consulta una factura por ID"""
    factura = facturas.get(factura_id)
    # Verificamos si la factura existe en la "base de datos" en memoria.
    if not factura:
        return jsonify({"error": "Factura no encontrada"}), 404

    # Si la factura existe, la retornamos.
    return jsonify(factura)


# Ejecutando la aplicación Flask
if __name__ == "__main__":
    app.run(debug=True, port=5000)
