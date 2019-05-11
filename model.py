from wtforms import Form, FloatField, validators,TextField,SelectField,DateField
from math import pi

class InputForm(Form):
    # A = TextField (
    #     label='Stock Name', default="AAPL",
    #     validators=[validators.InputRequired()])
    STOCK_NAME = SelectField('', choices = [('AAPL', 'APPLE'), 
      ('GOOG', 'GOOGLE'),('IBM', 'IBM'),('RHT', 'RED HAT')])
    