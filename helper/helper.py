import random
import string

class Helper():

    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def generate_random_email(self):
        return f"{self.generate_random_string(6)}@test.com"

    def generate_random_data(self):
        helper = Helper()
        email = helper.generate_random_email()
        password = helper.generate_random_string(10)
        name = helper.generate_random_string(10)
        user_data = {
            "email": email,
            "password": password,
            "name": name
            }
        return user_data