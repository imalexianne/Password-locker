

#!/usr/bin/env python3.6

from user import User
def create_user(fname,lname,e_mail,user_name,password):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,email,user_name,password)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()