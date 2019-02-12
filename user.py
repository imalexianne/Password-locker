



  
class User:
    """
    Class that generates new instances of contacts.
    """

    user_list = [] # Empty user list

    def __init__(self,first_name, last_name,e_mail,user_name,password):
        """
        __init__ method that helps us define properties for our objects.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.e_mail = e_mail
        self.user_name = user_name
       
        self.password = password 
       
       

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    @classmethod
    def user_exist(cls,user_name):
        '''
        Method that checks if a user exists from the user list.
        
        '''
        for user in cls.user_list:
            if user.user_name == user_name:
                    return True

        return False

    @classmethod
    def find_user_name(cls,user_name):
        '''
        Method that takes in a user_name and returns a user that matches that user_name.

        '''

        for user in cls.user_list:
            if user.user_name == user_name:
                return user