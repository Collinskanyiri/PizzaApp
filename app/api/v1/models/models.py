from app import db



class User(db.Model):
    """This will define all behaviours of the user

    Args:
        db ([type]): [description]
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column (db.String(255))
    location = db.Column(db.String(255))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    order = db.relationship('Order', backref='role', lazy="dynamic")
    def __repr__(self):
        return f'User {self.username}'


class Roles(db.Model):
    """This defines the users roles

    Args:
        db ([type]): [description]
    """
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref='role', lazy="dynamic")


class Pizza(db.Model):
    """This defines the behaviours of an individual pizza

    Args:
        db ([type]): [description]
    """
    __tablename__ = 'pizza'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    order = db.relationship('Order', backref='order', lazy="dynamic")

class Size(db.Model):
    """This will define the aspects of size

    Args:
        db ([type]): [description]
    """
    __tablename__ = 'size'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    order = db.relationship('Order', backref='order', lazy="dynamic")
    


class Toppings(db.Model):
    """This will define the topping aspects

    Args:
        db ([type]): [description]
    """
    __tablename__ = 'toppings'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    order = db.relationship('Order', backref='order', lazy="dynamic")


    
class Order(db.Model):
    """
    this is to def the user order
    Args:
     db([type]): [description]
    """
    __tablename__='order'
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'))
    size_id = db.Column(db.Integer, db.ForeignKey('size.id'))
    toppings_id = db.Column(db.Integer, db.ForeignKey('toppings.id'))
    
    def __init__(self,order_id, user_id, pizza_id, size_id, toppings_id) -> None:
        """
        Initialize the order module
        """
        self.id = len(order_id) + 1
        self.username = user_id
        self.pizza = pizza_id
        self.size = size_id
        self.toppings = toppings_id
    
        

    def save_order(self):
        """
        Method to register a user instance and update the data structure
        """
        order_record = dict(
            id=self.id,
            user_id=self.username,
            pizza_id=self.pizza,
            size_id=self.size,
            toppings_id=self.toppings,
            
            
        )
        self.order.update({
            self.id: order_record
        })