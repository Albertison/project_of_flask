from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask import redirect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')

@app.route("/")
def main():
    params = {}
    params['title'] = 'Начало'
    return render_template('first_page.html', **params)


@app.route("/registration", methods=['GET', 'POST'])
def registration():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/good')
    return render_template('registr.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')