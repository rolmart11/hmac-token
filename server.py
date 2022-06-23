from flask import Flask, request
import hmac
import hashlib
from Constant import SECRET_KEY

app = Flask(__name__)


@app.route('/generate-token', methods=['POST'])
def generate_token():
    # Checking if 'message' is in the request body
    if not request.get_json(force=True).get('message'):
        return {"errorMessage": "Missing field 'message' in request body"}, 400
    else:
        message = request.get_json(force=True)['message']
        hashed_message = hmac.new(SECRET_KEY, message.encode('utf-8'), hashlib.sha256)
        return {'message': message, 'signature': hashed_message.hexdigest()}, 201
    
    



if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)