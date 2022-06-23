import requests
from Constant import SECRET_KEY
import hmac
import hashlib
import random
import json

GENERIC_HEADER = {'Content-type': 'application/json'}

# A message bank to be picked from at random
test_message = ['Today I learned about HMAC tokens', 
                'I am passionate about reducing energy consumption', 
                'I initially though Apiaries had something to do with birds',
                'This should pass a test']

random_number = random.randint(0, 3)
random_message = test_message[random_number]
random_payload = {'message': random_message}

test_response = requests.post('http://localhost:5000/generate-token', data=json.dumps(random_payload), headers=GENERIC_HEADER)

# Extracting the token from the response
response_token = test_response.json()['signature']
# Generating a token on client side for validation
valid_compare_token = hmac.new(SECRET_KEY, random_message.encode('utf-8'), hashlib.sha256).hexdigest()
# Generating an invalid token on client side for failing
invalid_compare_token = hmac.new(bytes('not_a_secret', 'utf-8'), random_message.encode('utf-8'), hashlib.sha256).hexdigest()

# There should be an assertion error for the second 'assert'
assert hmac.compare_digest(valid_compare_token, response_token)
assert hmac.compare_digest(invalid_compare_token, response_token), "Designed to fail"
