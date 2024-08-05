import unittest
import requests
from app import create_app

class TestCase(unittest.TestCase):
    
    def test_success_user_response(self):
        app = create_app()
        # Start the test client
        self.app = app.test_client()
        username = "octocat"
        response = self.app.get(f"/{username}")
        self.assertEqual(response.status_code, 200)


    def test_success_user(self):
        app = create_app()
        self.app = app.test_client()
        username = ["octant"]
        for owner_login in username:
            response = self.app.get(f"/{owner_login}")
            if not response.json:
                print(f"Response is empty for user {username}")
            else:
                respose_user = response.json
                for user in respose_user:
                    expected_owner_name = user['owner']['login']
                self.assertEqual(owner_login, expected_owner_name, f"User {owner_login} matched '{expected_owner_name}'")


if __name__ == '__main__':
    unittest.main()
