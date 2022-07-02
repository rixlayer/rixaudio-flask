from . import db

class SubBrand(db.Model):
    __tablename__='subbrands'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    image = db.Column(db.String(60), nullable=False, default = 'defaultcity.jpg')
    products = db.relationship('Product', backref='subbrands', cascade="all, delete-orphan")

    def __repr__(self):
        str = "Id: {}, Name: {}, Image: {}\n" 
        str =str.format( self.id, self.name,self.image)
        return str

orderdetails = db.Table('orderdetails', 
    db.Column('orderid', db.Integer,db.ForeignKey('orders.id'), nullable=False),
    db.Column('productid',db.Integer,db.ForeignKey('product.id'),nullable=False),
    db.PrimaryKeyConstraint('orderid', 'productid') )

class Product(db.Model):
    __tablename__='product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False)
    price = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=True)
    model = db.Column(db.String(64), nullable=True)
    subb_id = db.Column(db.Integer, db.ForeignKey('subbrands.id'))
    
    def __repr__(self):
        str = "Id: {}, Name: {}, Description: {}, Image: {}, Price: {}, Weight: {}, Model: {}, SubBrand: {}\n" 
        str =str.format( self.id, self.name,self.desc,self.image, self.price, self.weight, self.model, self.subb_id)
        return str

class Order(db.Model):
    __tablename__='orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    name = db.Column(db.String(64))
    email = db.Column(db.String(128))
    totalcost = db.Column(db.Float)
    date = db.Column(db.DateTime)
    products = db.relationship("Product", secondary=orderdetails, backref="orders")
    
    def __repr__(self):
        str = "id: {}, Status: {}, Name: {}, Email: {}, Date: {}, Product: {}, Total Cost: {}\n" 
        str =str.format( self.id, self.status,self.name, self.email, self.date, self.products, self.totalcost)
        return str
