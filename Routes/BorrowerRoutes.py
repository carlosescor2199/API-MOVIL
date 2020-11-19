from API import app
from flask import request, jsonify
from DataBase import db
from Model.Borrower import Borrower, borrower_schema, borrowers_schema


@app.route('/borrower/register', methods=["POST"])
def register_borrower():
    fullname = request.json.get('fullname', None)
    CC = request.json.get('CC', None)
    phone = request.json.get('phone', None)
    amount = float(request.json.get('amount', None))
    percentage = float(request.json.get('percentage', None))
    months = int(request.json.get('months', None))

    user = Borrower.query.filter_by(CC=CC).first()
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
            "error": "La Cédula no puede estar vacia"
        }), 400
    if not phone:
        return jsonify({
            "error": "El teléfono no puede estar vacio"
        }), 400
    if not amount:
        return jsonify({
            "error": "El monto no puede estar vacio"
        }), 400
    if not percentage:
        return jsonify({
            "error": "El porcentaje no puede estar vacio"
        }), 400
    if not months:
        return jsonify({
            "error": "El número de meses no puede estar vacio"
        }), 400

    new_borrower = Borrower(fullname, CC, phone, amount, percentage, months)
    db.session.add(new_borrower)
    db.session.commit()
    return borrower_schema.jsonify(new_borrower)


@app.route('/borrower/edit/<id>', methods=["PUT"])
def edit_borrower(id):
    fullname = request.json.get('fullname', None)
    CC = request.json.get('CC', None)
    phone = request.json.get('phone', None)
    amount = float(request.json.get('amount', None))
    percentage = float(request.json.get('percentage', None))
    months = int(request.json.get('months', None))

    verifyUser = Borrower.query.filter_by(CC=CC).first()
    print(verifyUser)
    db.session.commit()
    if verifyUser:
        return jsonify({
            "error": "Esta cédula ya está registrada"
        }), 400
    if not fullname:
        return jsonify({
            "error": "El nombre completo no puede estar vacio"
        }), 400
    if not CC:
        return jsonify({
            "error": "La Cédula no puede estar vacia"
        }), 400
    if not phone:
        return jsonify({
            "error": "El teléfono no puede estar vacio"
        }), 400
    if not amount:
        return jsonify({
            "error": "El monto no puede estar vacio"
        }), 400
    if not percentage:
        return jsonify({
            "error": "El porcentaje no puede estar vacio"
        }), 400
    if not months:
        return jsonify({
            "error": "El número de meses no puede estar vacio"
        }), 400

    user = Borrower.query.get(id)
    user.fullName = fullname
    user.CC = CC
    user.phone = phone
    user.amount = amount
    user.percentage = percentage
    user.months = months
    db.session.commit()
    return borrower_schema.jsonify(user)


@app.route('/borrower/allborrowers', methods=["GET"])
def get_borrowers():
    all_borrowers = Borrower.query.all()
    result = borrowers_schema.dump(all_borrowers)
    return borrowers_schema.jsonify(result)
