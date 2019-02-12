#!/usr/bin/env python3.6

from credential import Credential
from user import User

def create_credential(account_name, account_user_name, account_password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(account_name, account_user_name, account_password)
    return new_credential

def create_user(first_name, last_name,e_mail,user_name,password):
    '''
    Function to create a new user
    '''
    new_user = User(first_name, last_name, e_mail,user_name,password)
    return new_user

def save_credentials(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()


def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()

def find_credential(account_name):
    '''
    Function that finds a credential by account_name and returns the credential
    '''
    return Credential.find_account_name(account_name)

def find_user(password):
    '''
    Function that finds a user by password and returns the user
    '''
    return User.find_user(password)    

def check_existing_credential(account_name):
    '''
    Function that check if a credential exists with that account_name and return a Boolean
    '''
    return Credential.credential_exist(account_name)

def check_existing_user(password):
    '''
    Function that check if a user exists with that user_name and return a Boolean
    '''
    return User.user_exist(password)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials()



def main():
    print("Hello Welcome to your credential list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
            print("Use these short codes : ca -create an account, lo -login, cc - create a new credential, dc - display credentials, fc -find a credential,dl -delete credential from the list,  ex -exit the credential list ")

            short_code = input().lower()

            if short_code == 'ca':
                    print("New User")
                    print("-"*10)

                    print ("first_name ....")
                    first_name = input()

                    print("last_name ...")
                    last_name = input()

                    print("e_mail ...")
                    e_mail= input()

                    print("user_name ...")
                    user_name = input()

                    print("password ...")
                    password= input()


                            

                    save_users(create_user(first_name, last_name, e_mail, user_name, password   )) # create and save new user.
                    print ('\n')
                    print(f"New User first_name: {first_name}, last_name: {last_name}, e_mail: {e_mail}, user_name: {user_name}, password: {password}  created")
                    print ('\n')



            elif short_code == 'lo':
               
                    print ("enter user_name ....")
                    user_name = input()

                    print("Enter password ...")
                    search_password = input()

                    if check_existing_user(search_password):
                            search_password = find_user(search_password)
                            
                       
                            print("WELLCOME")

                    else:
                            print("PLEASE CREATE AN ACCOUNT")

                       

            
            
            
            elif short_code == 'cc':
                    print("New Credential")
                    print("-"*10)

                    print ("account_name ....")
                    account_name = input()

                    print("account_user_name ...")
                    account_user_name = input()

                    print("account_password ...")
                    account_password = input()

                            

                    save_credentials(create_credential(account_name, account_user_name, account_password)) # create and save new credential.
                    print ('\n')
                    print(f"New Credential name: {account_name}, user_name: {account_user_name}, password: {account_password} created")
                    print ('\n')

            elif short_code == 'dc':

                    if display_credentials():
                            print("Here is a list of all your credentials")
                            print('\n')

                            for credential in display_credentials():
                                    print(f"{credential.account_name} {credential.account_user_name} {credential.account_password}")

                            print('\n')
                    else:
                            print('\n')
                            print("You dont seem to have any credential saved yet")
                            print('\n')

            elif short_code == 'fc':

                    print("Enter the account_name you want to search for")

                    search_account_name = input()
                    if check_existing_credential(search_account_name):
                            search_credential = find_credential(search_account_name)
                            print(f"{search_credential.account_name} {search_credential.account_user_name} {search_credential.account_password}")
                            print('-' * 20)

                            
                    else:
                            print("That credential does not exist")

            elif short_code == 'dl':

                    print("Enter the account_name you want to delete ")

                     
                    search_account_name = input()

                    if check_existing_credential(search_account_name):
                            search_password = find_credential(search_account_name)
                            
                       
                            print("CREDENTIAL DELETED")

                    else:
                            print("CREDENTIAL DOESN'T EXIST")


            elif short_code == "ex":
                    print("Bye .......")
                    break
            else:
                    print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':

    main()


