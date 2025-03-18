from flask import Flask, render_template,redirect, url_for
from flask_ckeditor import CKEditor
from forms import EmailForm, RegisterForm, LoginForm, CertificateForm
from flask_bootstrap import Bootstrap
import smtplib
import os
from dotenv import load_dotenv
from flask_login import login_user, current_user,logout_user, LoginManager, UserMixin
from sqlalchemy.orm import DeclarativeBase, Mapped,mapped_column
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import String, Integer

load_dotenv()

login = os.environ.get('user')
password = os.environ.get('password')

app = Flask(__name__)
ckeditor = CKEditor(app)
app.config['SECRET_KEY'] = 'the random string' 
Bootstrap(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)

class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI','sqlite:///posts.db')
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class User(UserMixin,db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    name: Mapped[str] = mapped_column(String,nullable=False)
    email : Mapped[str] = mapped_column(String, nullable=False,unique=True)
    password: Mapped[str] = mapped_column(String,nullable=False)

class Certificates(db.Model):
    id : Mapped[int] = mapped_column(Integer,primary_key=True)
    name : Mapped[str] = mapped_column(String,nullable=False)
    picture : Mapped[str] = mapped_column(String,nullable=False)
    describe : Mapped[str] = mapped_column(String,nullable=False)
    link : Mapped[str] = mapped_column(String,nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html',home=True,current_user=current_user)

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

@app.route('/certificates',methods=['GET','POST'])
def certificates():
    form = CertificateForm()
    certificates = db.session.execute(db.select(Certificates))
    certificates = certificates.scalars().all()
    if form.validate_on_submit():
        name = form.Cname.data
        pic = form.pic.data
        describe = form.describe.data
        link = form.link.data
        new_certificate = Certificates(name=name,picture=pic,describe=describe,link=link)
        db.session.add(new_certificate)
        db.session.commit()
        return redirect(url_for('certificates'))
    return render_template('certificates.html',form=form,certificates=certificates)

@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/register/<log>',methods=['GET','POST'])
def register(log):
    if log == 'register':
        form = RegisterForm()
    else:
        form = LoginForm()
    
    if form.validate_on_submit():
        if log =='register':
            name = form.username.data
            email = form.email.data
            password = form.password.data

            hash_pass = generate_password_hash(password=password,method='pbkdf2',salt_length=8)

            new_user = User(name=name,password=hash_pass, email=email)
            db.session.add(new_user)
            db.session.commit()

        elif log =='login':
            email = form.email.data
            password = form.password.data

            user = db.session.execute(db.select(User).where(User.email ==email)).scalar()
            if check_password_hash(user.password,password):
                login_user(user)
                return redirect(url_for('index'))
        

    return render_template('Register.html',form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

def send_mail(username,subject,email,message):
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=login,password='ckmctvanysxppyvl')
        connection.sendmail(from_addr=login,to_addrs=login,
                            msg=f"Subject:{subject}\n\n from:{email}{message}\nusername:{username}")


if __name__ == '__main__':
    app.run(debug=True)