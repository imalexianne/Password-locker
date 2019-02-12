import unittest
from user import User
class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the user class bahaviors.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user=User("first_name", "last_name","e_mail","user_name","password")


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name, "first_name")
        
        self.assertEqual(self.new_user.last_name, "last_name")
        self.assertEqual(self.new_user.e_mail, "e_mail")

        self.assertEqual(self.new_user.user_name, "user_name")
        self.assertEqual(self.new_user.password, "password")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("first_name","last_name","e_mail" , "user_name", "password") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_user_exist(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("first_name","last_name","e_mail" , "user_name", "password") # new user
        test_user.save_user()

        user_exists = User.user_exist("password")

        self.assertTrue(user_exists)

    def test_find_user_by_user_name(self):
        '''
        test to check if we can find a user by user_name and display information
        '''

        self.new_user.save_user()
        test_user = User("first_name","last_name","e_mail" , "user_name", "password") # new user
        test_user.save_user()

        found_user = User.find_user_name("user_name")

        self.assertEqual(found_user.first_name,test_user.first_name)
        self.assertEqual(found_user.last_name,test_user.last_name)

        self.assertEqual(found_user.e_mail,test_user.e_mail)
        self.assertEqual(found_user.password,test_user.password)
    

if __name__ == '__main__':
    unittest.main()