import json
from flask import Flask, request, render_template
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy.exc import IntegrityError
from datetime import timedelta 

from models import db, User, Pokemon, MyPokemon


''' Begin boilerplate code '''
def create_app():
  app = Flask(__name__, static_url_path='')
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
  app.config['SECRET_KEY'] = "MYSECRET"
  app.config['JWT_EXPIRATION_DELTA'] = timedelta(days = 7) 
  db.init_app(app)
  return app

app = create_app()

app.app_context().push()
''' End Boilerplate Code '''

''' Set up JWT here '''

''' End JWT Setup '''

# edit to query 50 pokemon objects and send to template
#Delete all of this

import csv
pokemon_list = []

with open('/workspace/info2602a2/App/pokemon.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        pokemon_list.append(Pokemon(name = line['name'],attack = line['attack'], defense = line['defense'],
        hp = line['hp'], height_m = line['height_m'], sp_attack = line['sp_attack'], sp_defense = line['sp_defense'],
        speed = line['speed'], type1 = line['type1'], type2 = line['type2'], weight_kg = line['weight_kg']
        ))

    
for obj in pokemon_list:
    if obj.type2 == "":
        obj.type2 = "None"
poke = pokemon_list
@app.route('/')
def index():
  return render_template('index.html',poke=poke) 

@app.route('/app')
def client_app():
  return app.send_static_file('app.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)