from DataBase import db, ma

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(100))
    CC = db.Column(db.String(10), unique=True)
    phone = db.Column(db.String(15))
    password = db.Column(db.Text)

    def __init__(self, fullName, CC, phone, password):
        self.fullName = fullName
        self.CC = CC
        self.phone = phone
        self.password = password

db.create_all()

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'fullName', 'CC', 'phone', 'password')

user_schema = UserSchema()
users_schema = UserSchema(many=True)