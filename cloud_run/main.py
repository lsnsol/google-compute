from flask import Flask, flash, request, redirect, url_for, make_response, jsonify
from flask_cors import cross_origin

app = Flask(__name__)
app.secret_key = 'k8smashers'

@app.route('/hello', methods=['GET'])
@cross_origin()
def hello_api():
  print ('Get call recieved')
  response = jsonify({'message': 'hello from cloud run'})
  return response

if __name__ == "__main__":
  app.run(debug=False, host="0.0.0.0", port=8080)