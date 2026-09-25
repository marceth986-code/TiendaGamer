import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
ARCHIVO = "datos.json"

def cargar_datos():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_datos(productos):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, indent=4, ensure_ascii=False)


@app.route('/')
def inicio():
    productos = cargar_datos()
    return render_template('index.html', productos=productos)

@app.route('/publicar', methods=['POST'])
def agregar_producto():
    productos = cargar_datos()
    
    nombre = request.form.get('nombre')
    categoria = request.form.get('categoria')
    
    try:
        precio = float(request.form.get('precio'))
        stock = int(request.form.get('stock'))
    except ValueError:
        return "Precio o stock inválido.", 400

    nuevo_id = max([p["id"] for p in productos], default=0) + 1

    nuevo_producto = {
        "id": nuevo_id,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock,
        "imagen": request.form.get('imagen') or "https://via.placeholder.com/200"
    }

    productos.append(nuevo_producto)
    guardar_datos(productos)
    return redirect(url_for('inicio'))

@app.route('/comprar', methods=['POST'])
def comprar_producto():
    productos = cargar_datos()
    prod_id = int(request.form.get('id'))
    cantidad = int(request.form.get('cantidad'))

    for p in productos:
        if p['id'] == prod_id:
            if p['stock'] >= cantidad:
                p['stock'] -= cantidad
                guardar_datos(productos)
                total = p['precio'] * cantidad
                return f"<h1>¡Compra realizada con éxito!</h1><p>Compraste {cantidad} unidad(es) de {p['nombre']} por un total de ${total}.</p><a href='/'>Volver al catálogo</a>"
            else:
                return f"<h1>Stock insuficiente</h1><p>Solo quedan {p['stock']} unidades disponibles.</p><a href='/'>Volver al catálogo</a>"

    return "Producto no encontrado", 404

if __name__ == '__main__':
    app.run(debug=True)