from flask import render_template, flash, redirect
from app import flask_app as app
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username':'testusr'}
    return render_template('lgtest.html',title='HOME:P2',user=user)
#def index():
#    return "Hello, World!"
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/index')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            #flash('Invalid username or password')
            #return redirect('/login')
            return render_template('login.html', form=form, error='Invalid username or password')
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = '/index'
        return redirect(next_page)
        #return redirect('/index')
    return render_template('login.html', form=form)
    #if form.validate_on_submit():
    #    flash('Login requested for user {}'.format(form.username.data))
    #    return redirect('/index')
    #return render_template('login.html',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/index')