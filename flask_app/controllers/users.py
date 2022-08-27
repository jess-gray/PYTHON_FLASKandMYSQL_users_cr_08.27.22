from flask_app import app
from flask import Flask, render_template, request, redirect, session 
from flask_app.models.user import User

@app.route('/users')
def user():
    return render_template('create.html')

@app.route('/users/new')
def route():
    all_users = User.get_all()
    return render_template('read_all.html', all_the_users = all_users)

@app.route('/new_user', methods = ["POST"])
def create_user():
    print(request.form)
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.create(data)
    return redirect('/users/new')
