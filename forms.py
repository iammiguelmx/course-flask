from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField

class ComentForm(Form):
    username = StringField('username')
    email =  EmailField('correo electronico')
    comment = TextField('comentario')