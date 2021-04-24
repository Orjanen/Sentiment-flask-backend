from textblob import TextBlob
from flask_cors import CORS, cross_origin
import os
import Tweets
from flask import Flask, jsonify, request

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/gettweets', methods=['POST'])
@cross_origin()
def getTweets():
    data = request.get_json()
    name = data['name']
    return Tweets.main.getTweets(name)

@app.route('/', methods=['GET'])
@cross_origin()
def hello():
    return jsonify({"response":"This is Sentiment Application"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
