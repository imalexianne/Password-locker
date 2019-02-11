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
        self.new_user=User("username","password")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username, "username")
        self.assertEqual(self.new_user.password, "password")
if __name__ == '__main__':
    unittest.main()