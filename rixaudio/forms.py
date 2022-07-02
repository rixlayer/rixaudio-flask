from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField
from wtforms.validators import InputRequired, email

# form used in cart
class CheckoutForm(FlaskForm):
    name = StringField("", validators=[InputRequired()], render_kw={"placeholder":"Full Name"})
    email = StringField("", validators=[InputRequired(), email()], render_kw={"placeholder":"Email ID"})
    phone = StringField("", validators=[InputRequired()], render_kw={"placeholder":"Phone number"})
    address = StringField("", validators=[InputRequired()], render_kw={"placeholder":"Shipping address"})
    submit = SubmitField("Make Payment")

