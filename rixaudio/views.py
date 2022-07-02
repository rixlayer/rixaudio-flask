from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import SubBrand, Product, Order
from datetime import datetime
from .forms import CheckoutForm
from . import db


bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    subbrands = SubBrand.query.order_by(SubBrand.name).all()
    p = Product.query.order_by(Product.name).all()
    return render_template('index.html', subbrands = subbrands, products = p)

@bp.route('/products/<subbid>/')
def subbs(subbid):
    subbrands = SubBrand.query.order_by(SubBrand.name).all()
    s = SubBrand.query.filter(SubBrand.id == subbid)
    p = Product.query.filter(Product.subb_id == subbid)
    return render_template('subb.html', products = p, subbrand = s, subbrands = subbrands)

@bp.route('/product/<pid>/')
def product(pid):
    p = Product.query.filter(Product.id == pid)
    subbrands = SubBrand.query.order_by(SubBrand.name).all()
    return render_template('product.html', product = p, subbrands = subbrands)


# Cart | Order Page
@bp.route('/order', methods=['POST','GET'])
def order():
    p_id = request.values.get('p_id')

    # retrieve order if there is one
    if 'orderid'in session.keys():
        order = Order.query.get(session['orderid'])
    else:
        order = None

    # create new order if not exist
    if order is None:
        order = Order(status = False, name='', email='', totalcost=0, date=datetime.now())
        try:
            db.session.add(order)
            db.session.commit()
            session['orderid'] = order.id
        except:
            print('failed at creating a new order')
            order = None
    
    # calcultate totalprice
    totalprice = 0
    if order is not None:
        for op in order.products:
            totalprice = totalprice + op.price
    
    # add item to cart if it doesn't exist
    if p_id is not None and order is not None:
        p = Product.query.get(p_id)
        if p not in order.products:
            try:
                order.products.append(p)
                db.session.commit()
            except:
                return 'Adding Product to Cart resulted in an error.'
            return redirect(url_for('main.order'))
        else:
            flash('This item has already been added to your cart')
            return redirect(url_for('main.order'))
    
    return render_template('order.html', order = order, totalprice = totalprice)


# Delete specific basket items
@bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    id=request.form['id']
    if 'orderid' in session:
        order = Order.query.get_or_404(session['orderid'])
        pdel = Product.query.get(id)
        print(pdel)
        try:
            order.products.remove(pdel)
            db.session.commit()
            return redirect(url_for('main.order'))
        except:
            return 'Problem deleting item from order'
    return redirect(url_for('main.order'))


# Delete Session
@bp.route('/deleteorder')
def deleteorder():
    if 'orderid' in session:
        del session['orderid']
        flash('All items deleted')
    return redirect(url_for('main.index'))


@bp.route('/checkout', methods=['POST','GET'])
def checkout():
    form = CheckoutForm() 
    if 'orderid' in session:
        order = Order.query.get_or_404(session['orderid'])
       
        if form.validate_on_submit():
            order.status = True
            order.name = form.name.data
            order.email = form.email.data
            totalcost = 0
            for p in order.products:
                totalcost = totalcost + p.price
            order.totalcost = totalcost
            order.date = datetime.now()
            try:
                db.session.commit()
                del session['orderid']
                flash('Thank you for shopping with us! Your shipment will be dispatched soon.')
                return redirect(url_for('main.index'))
            except:
                return 'There was an issue completing your order'
    return render_template('checkout.html', form = form)