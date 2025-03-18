from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

class EmailForm(FlaskForm):
    username = StringField("name", validators=[DataRequired()])
    subject = StringField("subject",validators=[DataRequired()])
    email = StringField("email",validators=[DataRequired()])
    message = CKEditorField("message",validators=[DataRequired()])
    submit = SubmitField('Send message')

class RegisterForm(FlaskForm):
    username = StringField('name',validators=[DataRequired()])
    email = StringField('email',validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired()])
    sumbit = SubmitField('submit')

class LoginForm(FlaskForm):
    email = StringField('email',validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired()])
    submit = SubmitField('submit')

class CertificateForm(FlaskForm):
    Cname = StringField('name',validators=[DataRequired()])
    pic = StringField('pic',validators=[DataRequired()])
    describe = StringField('describe',validators=[DataRequired()])
    link = StringField('link',validators=[DataRequired()])
    submit = SubmitField('Add new')

