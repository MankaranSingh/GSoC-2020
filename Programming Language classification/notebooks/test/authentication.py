from flask import redirect, url_for, redirect, current_app, request, jsonify
from ...models.users import User, Role, Category, SubCategory, ListItem, State, City
from .. import Authentication
from ... import db
from ...decorators import permission_required, admin_required
from ...utility.utilities import Utility
import smtplib
from datetime import datetime
from werkzeug import check_password_hash, generate_password_hash
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
import random


@Authentication.route('/v1.0/register',methods=['POST'])
def register():

    '''
        format - {'firstname':str, 'lastname':str, 'state':str, 'city':str, 'email':str, 'password':str, 'phone_number':str, 'confirm_pass':str}
    '''

    if request.method == 'POST':
        credentials = request.get_json()
        
        if Utility.validate_email(credentials['email']) is False:
            return jsonify(status='406', error='Invalid Email or Emailalready in use')
        
        if Utility.validate_phone_number(int(credentials['phone_number'])) is False:
            return jsonify(status='406', error='Invalid Phone Number or Phone Number already in use')

        if credentials['password'] != credentials['confirm_pass']:
            return jsonify(status='406', error="'Password' and 'Confirm Password' fields must match")
        
        state, city = Utility.validate_state_city(credentials['state'], credentials['city'])
        
        if not state:
            return jsonify(status='406', error='Invalid State')

        if not city:
            return jsonify(status='406', error='Invalid City')
        
        try:
            hashed_password = generate_password_hash(credentials['password'])
            user = User(firstname=credentials['firstname'], lastname=credentials['lastname'], email=credentials['email'], password=hashed_password, phone_number=credentials['phone_number'],state=credentials['state'],city=city)
            user.role = Role.query.filter_by(role_name = 'User').first()
            user.avtar_hash = user.generate_avtar_hash()
            db.session.add(user)
            db.session.commit()
            return jsonify(status='200',error='None', message='Registration Successful')
        
        except Exception as e:
            print(e)
            return jsonify(status='400',error='Bad Request')

@Authentication.route('/v1.0/login',methods=['POST'])
def login():

    '''
        format - {'email':str, 'password':str}
         
    '''
    
    if request.method == 'POST':
        credentials = request.get_json()

        user = User.query.filter_by(email = credentials['email']).first()
        if not user:
            return jsonify(status='406',error='Invalid email')
        elif not check_password_hash(user.password,credentials['password']):
            return jsonify(status='406',error='Invalid password')
        else:
            token = Utility.generate_auth_token(user)
            return jsonify(status='200',error='None', message='Login Successful', token=token.decode('ascii'))

@Authentication.route('/v1.0/log_check',methods=['POST'])
def login_check():
    credentials = request.get_json()
    response = Utility.is_logged_in(credentials['token'])
    return jsonify(status=response[0], message=response[1])

@Authentication.route('/v1.0/add_states',methods=['POST', 'GET'])
def add_states():

    state_object = State(name="Karnataka")
    db.session.add(state_object)
    db.session.commit()
    return "done bro"

@Authentication.route('/v1.0/add_cities',methods=['POST', 'GET'])
def add_cities():

    state_object = State.query.filter_by(name="Karnataka").first()
    city_object = City(name="Bengaluru", state=state_object)
    db.session.add(city_object)
    db.session.commit()
    return "done bro"

@Authentication.route('/v1.0/get_states',methods=['POST', 'GET'])
def get_states():

    states = State.query.all()
    return jsonify(states = [state.name for state in states])

@Authentication.route('/v1.0/get_cities',methods=['POST', 'GET'])
def get_cities():

    cities = City.query.all()
    return jsonify(cities = [city.name for city in cities])





                            

        
        
    




    
    
                            











