# from __future__ import unicode_literals

# from django.db import models

# # Create your models here.

from __future__ import unicode_literals
from django.db import models
import bcrypt
import re

class UserManager(models.Manager):
    # function to create the user, two parameters self and user posted data
    def creator(self, postData): 
        user = self.create(
        first_name = postData['first_name'],
        last_name = postData['last_name'],
        email = postData['email'],
        password = bcrypt.hashpw(
            postData['password'].encode(), 
            bcrypt.gensalt()),
        )
        return user

    # function to validate user posted data, two parameters self and user posted data
    def validate(self, postData):
        results = { 
            'status': True,
            'errors':[]
        }
        #first name validations
        if len(postData['first_name']) < 3:
            results['errors'].append('last name must not be less than 3 characters!!!!')
            results['status'] = False
        #last name validations
        if len(postData['last_name']) < 3:
            results['errors'].append('last name must not be less than 3 characters!!')
            results['status'] = False
        # email validations        
        if not re.match("[^@]+@[^@]+\.[^@]+", postData['email']):
            results['errors'].append('email invalid!!')
            results['status'] = False
        # password validations
        if len(postData['password']) < 3:
            results['errors'].append('Your password not less than 3 characters!!!!')
            results['status'] = False
        # password match validations    
        if postData['password'] != postData['confpw']:
            results['errors'].append('Passwords do not match!!')
            results['status'] = False
        # user non-existing validations  
        if len(self.filter(email = postData['email'])) > 0:
            results['errors'].append('The user already exists')  
            results['status'] = False
        # birthdate validation
        # now = datetime.datetime.now()
        # bday = datetime.datetime.strptime(
        #     postData['bday'], 
        #     '%Y-%m-%d'
        #     )
        # if bday > now:   # checking if birthdate if beyond Today!!!
        #     results['errors'].append("You cannot be born in the future!")
        #     results['status'] = False
        return results

    # function to create a logging-in user, two parameters self and user posted data
    def loginValidator(self, postData):
        results = {'status': True,'errors': [], 'user': None}
        users = self.filter(email = postData['email']) # check if email exists in db
        if len(users) < 1: # if user not in db
            results['status'] = False
        else: # otherwise encrypt his pw with bcrypt
            if bcrypt.checkpw(
                postData['password'].encode(), 
                users[0].password.encode()
                ):
                results['user'] = users[0] # compare with database user pwd hash
            else:
                results['status'] = False # if no match 
        return results

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()