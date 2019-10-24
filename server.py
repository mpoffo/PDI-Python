from flask import Flask, request as req, render_template_string, redirect, url_for
from flask_restful import Resource, Api
from flask_cors import CORS
import http
import requests

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


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if req.method == 'POST':
        if req.form['username'] != 'admin' or req.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))

    r = requests.get('http://localhost:4200/#/login')
    if r.status_code in [http.HTTPStatus.OK, http.HTTPStatus.CREATED, http.HTTPStatus.ACCEPTED]:
        return r.content
    else:
        return r.content


if __name__ == '__main__':
    app.run(port=5002, debug=True)
