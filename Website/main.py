from flask import Flask, render_template
from flask_ckeditor import CKEditor
from forms import EmailForm
from flask_bootstrap import Bootstrap


app = Flask(__name__)
ckeditor = CKEditor(app)
app.config['SECRET_KEY'] = 'the random string' 
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    form = EmailForm()

    return render_template('contact.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)