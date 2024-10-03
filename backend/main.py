from flask import request, jsonify
from config import app, db
from models import Person

@app.route('/persons', methods=['GET'])
def get_persons():
    persons = Person.query.all()
    return jsonify([{"id": person.id, "name": person.name, "roles": person.roles} for person in persons])

@app.route('/create_person', methods=['POST'])
def create_person():
    queries = request.args

    person = Person(name=queries['name'], roles=queries['roles'])
    
    if not queries.get('name') or not queries.get('roles'):
        return jsonify({"error": "Name and roles are required"})
    
    try:
        db.session.add(person)
        db.session.commit()
    except Exception as e:
        return jsonify({"error": str(e)})
    
    return jsonify({"person": person.to_json()})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)