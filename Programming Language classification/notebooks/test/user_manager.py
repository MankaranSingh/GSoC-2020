from flask import redirect, url_for, redirect, current_app, request, jsonify
from ...models.users import User, Role, Category, SubCategory, ListItem
from .. import User_manager
from ... import db
from ...decorators import permission_required, admin_required
from ...utility.utilities import Utility
import smtplib
from datetime import datetime
from werkzeug import check_password_hash, generate_password_hash
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)


@User_manager.route('/v1.0/users_profile',methods=['GET', 'POST', 'DELETE'])
def users_profile():
    
    return jsonify(status=200, message='under construction')
      
        
                    
        

    
        
        
        
        
    
        
            
                        
    
    
                            











