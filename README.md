# hmac-token

There are two python files one is a simple flask API, it is deployed on localhost port 5000 and has only one endpoint: 
POST /generate-token

and the other is a test that will validate the hmac token with a shared secret.

Sample Request:
curl -X POST \
  http://localhost:5000/generate-token \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: b7e7cd3d-71eb-9cd8-17d8-35a4733db63d' \
  -d '{
        "message": "This is only a test"
    }'

Sample Response:
{
    "message": "This is only a test",
    "signature": "5a646086c9d5a4023de1b6ecc2a7c286fba121f0c7db95abe5822b4a0c4cd84e"
}



Steps for running:
pip -r requirements.txt

Terminal 1
python server.py

Terminal 2
python test.py

The code is commented to explain what is happening where. I chose to go with the python hmac library as it ready out of the box and has a compare function that I used in the 'test.py' file. 