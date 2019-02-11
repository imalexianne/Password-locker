class Credential:
    """
    Class that generates new instances of credentials.
    """

    credential_list = [] # Empty credential list

    def __init__(self, account_name, account_user_name, account_password):
        """
        __init__ method that helps us define properties for our objects.
        """
        self.account_name = account_name
        self.account_user_name = account_user_name
        self.account_password = account_password
        
       

    def save_credential(self):

        '''
        save_credential method saves credential objects into credential_list
        '''

        Credential.credential_list.append(self)