import random
import string

class Helper():

    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def generate_random_email(self):
        return f"{self.generate_random_string(6)}@test.com"