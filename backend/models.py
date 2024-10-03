from config import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    roles = db.Column(db.String(80), unique=False, nullable=False)
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'roles': self.roles
        }