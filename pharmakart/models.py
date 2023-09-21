from pharmakart import db, login_manager, app
from flask_login import UserMixin
from datetime import datetime as dt

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """This is a class to create Users database using Python's Flask
    SQLAlchemy ORM using the db.model module"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, db.Sequence('users_id_seq'), primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    #image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(255), nullable=False)
    #posts =  db.relationship('Post', backref='author', lazy=True)

    def __init__(self, username, email, password):
        super().__init__()
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Staff(db.Model, UserMixin):
    """This is a class to create the Staff database using Python's Flask
    SQLAlchemy ORM using the db.model module"""
    st_id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    fullname = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=dt.utcnow)
    is_active = db.Column(db.Integer, nullable=False, default=0)
    avatar = db.Column(db.String(20), nullable=False, default='default.png')

    def __repr__(self):
        '''Representation of the Staff class when an instance is displayed'''
        return f'Staff("{self.st_id}", "{self.email}", "{self.is_active}")'
    

class Services(db.Model, UserMixin):
    """This is a class to create the Services database using Python's Flask
    SQLAlchemy ORM using the db.model module"""
    s_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    cost = db.Column(db.Float, nullable=False, default=0.0)

    def __repr__(self):
        '''Representation of the Services class when an instance is called'''
        return f'Services("{self.s_id}", "{self.name}", "{self.cost}")'


class Transactions(db.Model, UserMixin):
    """This class creates the Transactions database using Python's
    Flask SQLAlchemy ORM using the db.model module"""
    tran_id = db.Column(db.Integer, primary_key=True, nullable=False)
    tran_p_owner = db.Column(db.Integer, db.ForeignKey('users.id'),
                             nullable=False)
    tran_service = db.Column(db.Integer, db.ForeignKey('services.s_id'),
                             nullable=False)
    # tran_on_pet = db.Column(db.Integer, db.ForeignKey('pet.p_id'),
    #                         nullable=False)
    tran_date = db.Column(db.DateTime, nullable=False, default=dt.utcnow)
    tran_status = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        '''Representation of the Transaction class when an instance is
        called'''
        return f'Transaction("{self.tran_id}", "{self.tran_status}","{self.tran_date}")'


with app.app_context():
    db.create_all()