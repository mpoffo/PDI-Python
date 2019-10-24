from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin

app = Flask(__name__)
api = Api(app)
cors = CORS(app)


class Contacts(Resource):
    def get(self):
        return {'contacts': [
                              {'id': 1, 'nome': 'Marcio', 'mail': 'marcio@gmail.com'},
                              {'id': 2, 'nome': 'Roberta', 'mail': 'roberta@gmail.com'}
                            ]}


api.add_resource(Contacts, '/contacts')  # Route_1

if __name__ == '__main__':
    app.run(port=5002)
