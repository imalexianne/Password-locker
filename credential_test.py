import unittest


from credential import Credential
class TestCredential(unittest.TestCase):
    """
    Test class that defines test cases for the credential class bahaviors.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential=Credential("account_name", "account_user_name", "account_password")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credential_list = []


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.account_name, "account_name")
        self.assertEqual(self.new_credential.account_user_name, "account_user_name")
        self.assertEqual(self.new_credential.account_password, "account_password")

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the credential list
        '''
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credential.credential_list),1)

    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple credential
        objects to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("account_name", "account_user_name", "account_password") # new credential
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential from our credential list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("account_name","account_user_name","account_password") # new credential
        test_credential.save_credential()

        self.new_credential.delete_credential()# Deleting a credential object
        self.assertEqual(len(Credential.credential_list),1)

    def test_find_credential_by_account_name(self):
        '''
        test to check if we can find a credential by account_name and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credential("account_name","account_user_name","account_password") # new credential
        test_credential.save_credential()

        found_credential = Credential.find_account_name("account_name")

        self.assertEqual(found_credential.account_user_name,test_credential.account_user_name)
        self.assertEqual(found_credential.account_password,test_credential.account_password)

    def test_credential_exist(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credential.save_credential()
        test_credential = Credential("account_name","account_user_name","account_password") # new credential
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("account_name")

        self.assertTrue(credential_exists)

    
    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credential.display_credentials(),Credential.credential_list)

if __name__ == '__main__':
    unittest.main()