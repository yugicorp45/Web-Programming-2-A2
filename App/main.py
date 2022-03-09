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
'''
import csv

pokemon_list = []
p_name = ""
atk = 0
defen = 0
hp_health = 0
spatk = 0
spdef = 0
p_speed = 0
weight = 1.0
height = 1.0
type_1 = ""
type_2 = ""
with open('/workspace/info2602a2/App/pokemon.csv','r') as csv_file:
  csv_reader = csv.DictReader(csv_file)

  for line in csv_reader:
    p_name = line['name']
    if p_name == "":
      p_name = None

    atk = line['attack']
    if atk =="":
      atk = None
        
    defen = line['defense']
    if defen == "":
      defen = None

    hp_health = line['hp']
    if hp_health == "":
      hp_health = None

    spatk = line['sp_attack']
    if spatk =="":
      spatk = None
        
    spdef = line['sp_defense']
    if spdef == "":
      spdef = None

    p_speed = line['speed']
    if p_speed == "":
      p_speed = None

    type_1 = line['type1']
    if type_1 =="":
      type_1 = None
        
    defen = line['defense']
    if defen == "":
      defen = None


    weight = line['weight_kg']
    if weight == "":
      weight = None

    height = line['height_m']
    if height =="":
      height = None
        
    type_2 = line['type2']
    if type_2 == "":
      type_2 = None

    pokemon_list.append(Pokemon(name = p_name, attack = atk, defense = defen,
    hp = hp_health, height_m = height, sp_attack = spatk, sp_defense = spdef,
    speed = p_speed, type1 = type_1, type2 = type_2, weight_kg = weight
    ))
poke = pokemon_list
'''
@app.route('/')
def index():
  poke = Pokemon.query.filter_by
  return render_template('index.html') 

@app.route('/app')
def client_app():
  return app.send_static_file('app.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)