from flask import Flask,request,current_app, flash, jsonify, make_response, redirect, request, url_for
app = Flask(__name__)
import json
import random
from flask_cors import CORS
CORS(app)

@app.route("/")
def index():
    num = random.randint(1, 100)
    fotos=['https://urbanluxury.b-cdn.net/wp-content/uploads/2022/09/URBAN_LUXURY-1031-683x1024.jpg']
    fot=random.choice(fotos)
    data={"id":str(num),'nombre':'pantalon','descripcion':'es un pantalon','stock':'1','precio':'500','foto':fot}
    data=json.loads(json.dumps(data).encode('utf-8').decode('ascii'))
    return make_response(jsonify(data), 200)

