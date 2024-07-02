# server/app.py

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Pet

# add this view after index()

@app.router('/pets/<int:id>')
def pet_by_id(id):
    pet = Pet.query.filter(Pet.id == id).first()
    response_body = f'<p>{pet.name} {pet.species}</p>'

    response = make_response(response_body, 200)

    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
