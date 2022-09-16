"""
A Sample Web-DB Application for DB-DESIGN lecture
Copyright (C) 2022 Yasuhiro Hayashi
"""
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length
from flaskdb.widgets import ButtonField

class LoginForm(FlaskForm):
    username = StringField(
        "User Name",
        validators = [
            DataRequired(message="User Name is required."),
            length(max=64, message="User Name should be input within 64 characters."),
        ],
    )
    password = PasswordField(
        "Password",
        validators = [
            DataRequired(message="Password is required."),
        ],
    )
    cancel = ButtonField("Cancel")
    submit = SubmitField("Login")

    def copy_from(self, user):
        self.username.data = user.username
        self.password.data = user.password

    def copy_to(self, user):
        user.username = self.username.data
        user.password = self.password.data

class AddItemForm(FlaskForm):
    itemname = StringField(
        "Item Name",
        validators = [
            DataRequired(message="Item Name is required."),
        ],
    )
    price = IntegerField(
        "Price",
        validators = [
            DataRequired(message="Price is required."),
        ],
    )
    cancel = ButtonField("Cancel")
    submit = SubmitField("Submit")

    def copy_from(self, item):
        self.itemname.data = item.itemname
        self.price.data = item.price

    def copy_to(self, item):
        item.itemname = self.itemname.data
        item.price = self.price.data

class ErrorForm(FlaskForm):
    errorcode = StringField(
        "Error Code",
        validators = [
            DataRequired(message="Error Code is required."),
        ],
    )
    errordetail = StringField(
        "Error Detail",
        validators = [
            DataRequired(message="Error Detail is required."),
        ],
    )
    fixedcode = StringField(
        "Fixed Code",
        validators = [
            DataRequired(message="Fixed Code is required."),
        ],
    )
    solve = StringField(
        "Solve",
        validators = [
            DataRequired(message="Solve is required."),
        ],
    )
    keyword = StringField(
        "Keyword",
        validators = [
            DataRequired(message="Keyword is required."),
        ],
    )
    
    cancel = ButtonField("Cancel")
    submit = SubmitField("Submit")

    def copy_from(self, hoge):
        self.errorcode.data = hoge.errorcode
        self.errordetail.data = hoge.errordetail
        self.fixedcode.data = hoge.fixedcode
        self.solve.data = hoge.solve
        self.keyword.data = hoge.keyword

    def copy_to(self, hoge):
        hoge.errorcode = self.errorcode.data
        hoge.errordetail = self.errordetail.data
        hoge.fixedcode = self.fixedcode.data
        hoge.solve = self.solve.data
        hoge.keyword = self.keyword.data

class SearchItemForm(FlaskForm):
    itemname = StringField(
        "Item Name",
        validators = [
            DataRequired(message="Item Name is required."),
        ],
    )
    cancel = ButtonField("Cancel")
    submit = SubmitField("Submit")

    def copy_from(self, item):
        self.itemname.data = item.itemname

    def copy_to(self, item):
        item.itemname = self.itemname.data

class CheckOutForm(FlaskForm):
    cancel = ButtonField("Cancel")
    submit = SubmitField("Checkout")
