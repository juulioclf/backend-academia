from academia.ext.database import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import func

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=func.now())
    type = db.Column(db.String(50), nullable=False, default="teacher")

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'created_at': self.created_at.isoformat(),  # converte para string ISO
            'type': self.type
            # Adicione outros campos, se necessário
        }
