from flask import redirect, url_for, redirect, current_app, request, jsonify
from ...models.users import User, Role, Category, SubCategory, ListItem
from .. import Category_handler
from ... import db
from ...decorators import permission_required, admin_required
from ...utility.utilities import Utility
import smtplib
from datetime import datetime
from werkzeug import check_password_hash, generate_password_hash
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)


@Category_handler.route('/v1.0/categories',methods=['GET', 'POST', 'PUT', 'DELETE'])
def categories():

    if request.method == 'POST':

        '''
            format - {
                        "categories" : [{"name":str, "image":str}, {"name":str, "image":str}, ...]
                     }
        '''
        
        category_list = request.get_json()['categories']
        for category in category_list:
            try:
                item = Category(name=category['name'], image=category['image'])
                db.session.add(item)
            except:
                continue
        db.session.commit()
        return jsonify(status=200, message='Categories added successfully')

    if request.method == 'GET':

        category_list = Category.query.all()
        json = {'status':'200', 'categoies':[{'id':category.id, 'name':category.name, 'image':category.image, 'subcategories':[{'id':subcategory.id, 'name':subcategory.name} for subcategory in category.subcategories] } for category in category_list]}
        return jsonify(json)

    if request.method == 'PUT':

        '''
            format - {
                        "categories" : [{"current_name":str, "new_name":str, "new_image":str}, {"current_name":str, "new_name":str, "new_image":str}, ...]
                     }
        '''

        category_list = request.get_json()['categories']
        for category in category_list:
            item = Category.query.filter_by(name=category['current_name']).first()
            if item:
                if category['new_name'] != '':
                    item.name = category['new_name']
                if category['new_image'] != '':
                    item.image = category['new_image']
                db.session.commit()
        db.session.commit()
        return jsonify(status=200, message='items updated successfully')

    if request.method == 'DELETE':

        '''
            format - {
                        "categories" : [{"name":str}, {"name":str}, ...]
                     }
        '''
        category_list = request.get_json()['categories']
        for category in category_list:
            item = Category.query.filter_by(name=category['name']).first()
            if item:
                db.session.delete(item)
        db.session.commit()
        return jsonify(status=200, message='items deleted successfully')


@Category_handler.route('/v1.0/categories/subscriptions',methods=['GET', 'POST', 'DELETE'])
def category_subscriptions():

    if request.method == 'POST':

        '''
            format - {
                        "category" : str, token : str
                     }
        '''
        json = request.get_json()
        token = request.get_json()['token']
        category_item = Category.query.filter_by(name=json['category']).first()
        if not category_item:
            return jsonify(status=404, message='category not found')
        user = Utility.get_user_by_token(token)
        if not user:
            return jsonify(status=404, message='user not found')
        if user in category_item.subscribers:
            return jsonify(status=400, message='duplicate subscription')
        category_item.subscribers.append(user)
        db.session.commit()
        return jsonify(status=200, message='subscription successfull')

    if request.method == 'DELETE':
        
        '''
            format - {
                        "category" : str, token : str
                     }
        '''                                      
        json = request.get_json()
        token = request.get_json()['token']
        category_item = Category.query.filter_by(name=json['category']).first()
        if not category_item:
            return jsonify(status=404, message='category not found')
        user = Utility.get_user_by_token(token)
        if not user:
            return jsonify(status=404, message='user not found')
        if user in category_item.subscribers:
            category_item.subscribers.remove(user)
            db.session.commit()
            return jsonify(status=200, message='user unsubscribed successfully')
        return jsonify(status=404, message='subscriber not found')

    if request.method == 'GET':
        '''
            format - {
                        "category" : str, "action" : "(is_subscribed/count/get_subscribed_users)", token : str 
                     }
        '''
        json = request.get_json()
        token = request.get_json()['token']
        category_item = Category.query.filter_by(name=json['category']).first()
        if not category_item:
            return jsonify(status=404, message='category not found')
        if json['action'] == 'is_subscribed':
            user = Utility.get_user_by_token(token)
            if not user:
                return jsonify(status=404, message='user not found')
            if user in category_item.subscribers:
                return jsonify(status=200, message='True')
            return jsonify(status=200, message='False')
        if json['action'] == 'count':
            return jsonify(status=200, meessage=len(category_item.subscribers))
        if json['action'] == 'get_subscribed_users':
            return jsonify(status='200', users=[{"name" : subscriber.firstname + ' ' + subscriber.lastname} for subscriber in category_item.subscribers])
        return jsonify(status=400, message='action not supported')


      
        
                    
        

    
        
        
        
        
    
        
            
                        
    
    
                            











