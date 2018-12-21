from flask import Flask
import requests
from bs4 import BeautifulSoup
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
domain = 'https://www.caelum.com.br'

@app.route("/")
def home():
    return "Welcome to this API xD"

@app.route("/instructors")
def instructors():
    response = requests.get(domain+'/instrutores')
    rawHTML = BeautifulSoup(response.text, 'html.parser').select('figure')
    
    instructor = map(lambda instrutor: {
        'photo': domain+instrutor.find('img')['src'],
        'name': instrutor.find('figcaption').text
    }, rawHTML)

    return json.dumps(list(instructor)).encode('utf-8')