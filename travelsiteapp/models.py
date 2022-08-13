from asyncio.windows_events import NULL
from tkinter import CASCADE
from django.db import models
import re
import bcrypt

# Create your models here.


class UserManager(models.Manager):
    def registrationValidator(self, forminfo):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        validationErrors ={}

        if len(forminfo['fname']) < 2:
            validationErrors['FIRSTname'] = "First name must be at least 2 characters"
        if len(forminfo['lname']) < 2:
            validationErrors['LASTname'] = "First name must be at least 2 characters"
        if len(forminfo['email']) < 1:
            validationErrors['email'] = 'Email is required!'
        elif not EMAIL_REGEX.match(forminfo['email']):
            validationErrors['emailFormat'] = "Email is invalid"
        else:
            usersWithEmail = User.objects.filter(email = forminfo['email'])
            if len(usersWithEmail) > 0:
                validationErrors['emailTaken'] = "Email is taken, please try another email address."
        
        if len(forminfo['uname']) < 4:
            validationErrors['userNameTooShort'] = 'User name must be at lease 4 Characters'

        if len(forminfo['pass']) < 8:
            validationErrors['passTooShort'] = "Password must be at least 8 chracters."

        if forminfo['pass'] != forminfo['cpass']:
            validationErrors['passMatch'] = "Passwords do not match"

        return validationErrors
        # if len(validationErrors) == 0:
        #     validationErrors['sucess'] = "Sign up was sucessful!"

    def loginValidator(self, forminfo):
        errors = {}
        if len(forminfo['email']) < 1: 
            errors['emailReq']= 'Email is required to login'
        emailsExist = User.objects.filter(email = forminfo['email'])
        if len(emailsExist) ==0:
            errors['noEmail'] = "This email is not registered."
        
        else:
            user = emailsExist[0]
            if not bcrypt.checkpw(forminfo['password'].encode(), user.password.encode()):
                errors['pw'] = "Password does not match"
        
        return errors

class User(models.Model):
    firstName = models.CharField(max_length= 255)
    lastName = models.CharField(max_length= 255)
    email = models.CharField(max_length= 255)
    username = models.CharField(max_length= 255,  null=True)
    password = models.CharField(max_length= 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Trip(models.Model):
    city = models.CharField(max_length= 255)
    country = models.CharField(max_length= 255)
    continent = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length= 255)
    creator = models.ForeignKey(User, related_name = 'trips_uploaded',on_delete= CASCADE, null=True)
    favoriter = models.ManyToManyField(User, related_name= 'fav_trips')
    photo = models.ImageField(upload_to='trips/', null=True, blank =True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

# class Like(models.Model):

# class Continent(models.Model):
#     name = models.CharField(max_length= 255)
#     trip = models.ForeignKey(Trip, related_name="continent", on_delete= models.DO_NOTHING, null=True)