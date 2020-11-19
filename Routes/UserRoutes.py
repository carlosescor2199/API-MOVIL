from API import app
from flask import request, jsonify
from DataBase import db
from Model.User import User, user_schema, users_schema
import bcrypt


@app.route('/signup', methods=["POST"])
def signUp():
    fullname = request.json.get('fullname', None)
    CC = request.json.get('CC', None)
    phone = request.json.get('phone', None)
    password = request.json.get('password', None)
    confirm_password = request.json.get('confirm_password', None)

    user = User.query.filter_by(CC=CC).first()
    if user:
        return jsonify({
            "error": "Esta cédula ya está registrada"
        }), 400
    if not fullname:
        return jsonify({
            "error": "El nombre completo no puede estar vacio"
        }), 400
    if not CC:
        return jsonify({
            "error": "La cédula no puede estar vacia"
        }), 400
    if not phone:
        return jsonify({
            "error": "El Telefono no puede estar vacio"
        }), 400
    if not password:
        return jsonify({
            "error": "La contraseña no puede estar vacía"
        }), 400
    if not confirm_password:
        return jsonify({
            "error": "Confirmar contraseña no puede estar vacio"
        }), 400
    if password != confirm_password:
        return jsonify({
            "error": "Las contraseñas no coinciden"
        }), 400

    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    new_user = User(fullname, CC, phone, hashed)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)


@app.route('/login', methods=["POST"])
def Login():
    CC = request.json.get('CC', None)
    password = request.json.get('password', None)

    if not CC:
        return jsonify({
            "error": "La cédula no puede estar vacia"
        }), 400
    if not password:
        return jsonify({
            "error": "La contraseña no puede estar vacía"
        }), 400

    user = User.query.filter_by(CC=CC).first()

    if not user:
        return jsonify({
            "error": "Usuario no encontrado"
        }), 400

    if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return jsonify({
            "error": "Contraseña incorrecta"
        })

    db.session.commit()
    return user_schema.jsonify(user)


@app.route('/allUser', methods=["GET"])
def UsersTable():
    all_users = User.query.all()
    result = users_schema.dump(all_users)

    return users_schema.jsonify(result)


@app.route('/editUser/<id>', methods=["PUT"])
def editUser(id):
    editUser = User.query.get(id)

    fullName = request.json['fullName']
    CC = request.json['CC']
    phone = float(request.json['phone'])
    password = request.json['password']

    editUser.fullName = fullName
    editUser.CC = CC
    editUser.phone = phone
    editUser.password = password

    db.session.commit()
    return user_schema.jsonify(editUser)


@app.route('/deleteUser/<id>', methods=["DELETE"])
def deleteUser(id):
    deleteUser = User.query.get(id)
    db.session.delete(deleteUser)
    db.session.commit()
    return user_schema.jsonify(deleteUser)
