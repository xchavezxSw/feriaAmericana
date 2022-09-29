from flask import Flask,request,current_app, flash, jsonify, make_response, redirect, request, url_for
app = Flask(__name__)
import json
import random
@app.route("/")
def index():
    num = random.randint(1, 100)
    fotos=['https://urbanluxury.b-cdn.net/wp-content/uploads/2022/09/URBAN_LUXURY-1031-683x1024.jpg']
    fot=random.choice(fotos)
    data=[str(num),'pantalon','es un pantalon','1','500',fot]
    data=json.loads(json.dumps(data))
    return make_response(jsonify(data), 200)

