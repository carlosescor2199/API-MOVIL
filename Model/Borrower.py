from DataBase import db, ma


class Borrower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    CC = db.Column(db.String(10), unique=True)
    phone = db.Column(db.String(15))
    amount = db.Column(db.Float(15))
    percentage = db.Column(db.Float(3))
    months = db.Column(db.Integer)

    def __init__(self, fullname, CC, phone, amount, percentage, months):
        self.fullname = fullname
        self.CC = CC
        self.phone = phone
        self.amount = amount
        self.percentage = percentage
        self.months = months


db.create_all()


class BorrowerSchema(ma.Schema):
    class Meta:
        fields = ('id', 'fullname', 'CC', 'phone', 'amount', 'percentage', 'months')


borrower_schema = BorrowerSchema()
borrowers_schema = BorrowerSchema(many=True)
