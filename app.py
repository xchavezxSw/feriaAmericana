from flask import Flask,request,current_app, flash, jsonify, make_response, redirect, request, url_for
app = Flask(__name__)
import json
import random
from flask_cors import CORS
CORS(app)

@app.route("/")
def index():
    output=[]
    output.append({"id":"1",'nombre':'Jean','descripcion':'Pantalon de Jean deportivo','stock':'1','precio':'500','foto':'https://urbanluxury.b-cdn.net/wp-content/uploads/2022/09/URBAN_LUXURY-1031-683x1024.jpg','categoria':'mujer'})
    output.append({"id":"3",'nombre':'Pantalon gabardina','descripcion':'Pantalon de gabardina','stock':'1','precio':'500','foto':"https://urbanluxurymarcas.com/wp-content/uploads/2022/09/URBAN_LUXURY-291-500x750.jpg",'categoria':'hombres'})
    output.append({"id":"2",'nombre':'zapatillas','descripcion':'zapatillas para el cali','stock':'1','precio':'500','foto':"https://urbanluxurymarcas.com/wp-content/uploads/2022/08/URBAN_LUXURY-1471-500x750.jpg",'categoria':'ninos'})
    data=json.loads(json.dumps(output).encode('utf-8').decode('ascii'))
    return make_response(jsonify(data), 200)

@app.route("/imagen")
def imagen(id):
    output=[]
    if id=="1":
        output.append({"id":"1",'nombre':'Jean','descripcion':'Pantalon de Jean deportivo','stock':'1','precio':'500','foto':'https://urbanluxury.b-cdn.net/wp-content/uploads/2022/09/URBAN_LUXURY-1031-683x1024.jpg','categoria':'mujer'})
        output.append({"id":"1",'nombre':'Pantalon gabardina','descripcion':'Pantalon de gabardina','stock':'1','precio':'500','foto':"https://urbanluxurymarcas.com/wp-content/uploads/2022/09/URBAN_LUXURY-291-500x750.jpg",'categoria':'hombres'})
        output.append({"id":"1",'nombre':'zapatillas','descripcion':'zapatillas para el cali','stock':'1','precio':'500','foto':"https://urbanluxurymarcas.com/wp-content/uploads/2022/08/URBAN_LUXURY-1471-500x750.jpg",'categoria':'ninos'})
    data=json.loads(json.dumps(output).encode('utf-8').decode('ascii'))
    return make_response(jsonify(data), 200)
