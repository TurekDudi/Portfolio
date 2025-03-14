from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

class EmailForm(FlaskForm):
    username = StringField("name", validators=[DataRequired()])
    subject = StringField("subject",validators=[DataRequired()])
    email = StringField("email",validators=[DataRequired()])
    message = CKEditorField("message",validators=[DataRequired()])
    submit = SubmitField('Send message')