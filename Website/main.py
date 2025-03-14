from flask import Flask, render_template
from flask_ckeditor import CKEditor
from forms import EmailForm
from flask_bootstrap import Bootstrap
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

login = os.environ.get('user')
password = os.environ.get('password')

app = Flask(__name__)
ckeditor = CKEditor(app)
app.config['SECRET_KEY'] = 'the random string' 
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html',home=True)

@app.route('/contact',methods=['GET','POST'])
def contact():
    form = EmailForm()
    if form.validate_on_submit():
        email = form.email.data
        subject = form.subject.data
        message = form.message.data
        username = form.username.data
        print(message)
        send_mail(username,subject,email,message)

    return render_template('contact.html',form=form)

@app.route('/certificates')
def certificates():
    return render_template('certificates.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

def send_mail(username,subject,email,message):
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=login,password='ckmctvanysxppyvl')
        connection.sendmail(from_addr=login,to_addrs=login,
                            msg=f"Subject:{subject}\n\n from:{email}{message}\nusername:{username}")


if __name__ == '__main__':
    app.run(debug=True)