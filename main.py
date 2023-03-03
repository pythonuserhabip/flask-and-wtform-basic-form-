from flask import Flask, render_template, url_for, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class MyForm(FlaskForm):
    first_name = StringField('Adınız:', validators=[DataRequired()])
    last_name = StringField('Soyadınız:', validators=[DataRequired()])
    submit = SubmitField('Gönder')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        return redirect(url_for('success', first_name=first_name, last_name=last_name))
    return render_template('index.html', form=form)

@app.route('/success/<first_name>/<last_name>')
def success(first_name, last_name):
    return f"<h1>Teşekkürler, {first_name} {last_name}!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
