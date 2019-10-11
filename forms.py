from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SelectField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class stan(FlaskForm):
    amount = StringField("Rent amount per month for first year(11 months)", validators = [DataRequired()])
    duration = StringField("Total duration in years (1 year = 11 months)", validators = [DataRequired()])
    interest = StringField("% increase in rent every year", validators = [DataRequired()], default = "10")
    captcha = StringField("captcha", validators = [DataRequired()])
    submit = SubmitField("Submit")
