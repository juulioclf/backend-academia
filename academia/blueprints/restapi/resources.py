from flask import abort, jsonify, request
from flask_restful import Resource

from academia.models import User
from academia.ext.database import db


class UserResource(Resource):

    def get(self):
        try:
            users = User.query.all()
            if not users:
                return jsonify({"users": []}), 200
            return jsonify({"users": [user.to_dict() for user in users]})
        except Exception as e:
            print(f"Error: {e}")
            return jsonify({"message": "Internal Server Error"}), 500

    
    def post(self):
        try:
            data = request.get_json()
            required_fields = ['email', 'username', 'password']

            for field in required_fields:
                if field not in data:
                    return jsonify({"message": f"Campo obrigatório ausente: {field}"}), 400

            existing_user = User.query.filter_by(email=data['email']).first()

            if existing_user:
                return jsonify({"message": "Endereço de e-mail já está em uso"}), 409


            new_user = User(
                email=data['email'],
                username=data['username'],
                password=data['password'],
                type=data.get('type', 'teacher') 
            )

            db.session.add(new_user)
            db.session.commit()

            return jsonify({"message": "Usuário criado com sucesso", "user": new_user.to_dict()}), 201

        except Exception as e:
            print(f"Error: {e}")
            return jsonify({"message": "vish raapaz..."}), 500

            
class UserItemResource(Resource):
    def get(self, id):
        try:
            user = User.query.get(id)
            if user is None:
                return jsonify({"message": "User not found"}), 409
            return jsonify(user.to_dict())

        except Exception as e:
            print(f"Error: {e}")
            return jsonify({"message": "vish raapaz..."}), 500
