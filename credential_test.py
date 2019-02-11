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
        self.new_credential.save_credential() # saving the new contact
        self.assertEqual(len(Credential.credential_list),1)

if __name__ == '__main__':
    unittest.main()