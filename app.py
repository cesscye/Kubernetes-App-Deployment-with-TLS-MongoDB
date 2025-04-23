from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection
mongo_host = os.environ.get('MONGO_HOST', 'mongo-0.mongo.flask.svc.cluster.local')
mongo_port = int(os.environ.get('MONGO_PORT', 27017))

client = MongoClient(mongo_host, mongo_port)
db = client['demo_db']
collection = db['visits']

@app.route('/', methods=['GET'])
def index():
    count = collection.count_documents({})
    return f"Welcome! Total visits: {count}\n"

@app.route('/visit', methods=['POST'])
def visit():
    name = request.json.get('name', 'anonymous')
    collection.insert_one({'name': name})
    return jsonify({'message': f'Visit recorded for {name}'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
