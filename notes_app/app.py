from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    role = "normal"
    notes = ["Nota 1", "Nota 2", "Nota 3"]
    dict1 = {"nombre" : "dict1", "fechadc": "06-14-2025", "descripcion": "descripcion de dict1"}
    dict2 = {"nombre" : "dict2", "fechadc": "06-14-2025", "descripcion": "descripcion de dict2"}
    dict3 = {"nombre" : "dict3", "fechadc": "06-14-2025", "descripcion": "descripcion de dict3"}
    return render_template("index.html", role=role, notes=notes, dict1=dict1, dict2=dict2, dict3=dict3)

@app.route("/about")
def about():
    return "Esto es una app de notas."

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        return "Formulario de contacto enviado correctamente." , 201
    return "Página de contacto."

@app.route("/api/info")
def api_info():
    data = {
        "nombre" : "Notes App",
        "version" : "1.1.1"
    }
    return jsonify(data), 200