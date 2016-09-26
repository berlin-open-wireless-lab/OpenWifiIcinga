from wtforms import Form, TextField, IntegerField, PasswordField, BooleanField

class IcingaConfForm(Form):
    url = TextField('url')
    login = TextField('login')
    password = PasswordField('password')
    port = IntegerField('port')
    verify = BooleanField('verify')
