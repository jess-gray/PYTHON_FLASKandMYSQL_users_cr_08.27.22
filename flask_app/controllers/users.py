from flask_app import app
from flask import Flask, render_template, request, redirect, session 
from flask_app.models.user import User

@app.route('/users') #this is the page/form to add a new user
def user():
    return render_template('create.html')

@app.route('/users/new') #this is to show ALL users (also home)
def route():
    all_users = User.get_all()
    return render_template('read_all.html', all_the_users = all_users)

@app.route('/new_user', methods = ["POST"]) #this is actually adding the new user
def create_user():
    print(request.form)
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    show_user = User.create(data)
    return redirect(f'/read/{show_user}') #the user.create(data) is grabbing the info, making into a variable we can use it in the redirect

@app.route('/read/<int:id>') #this is to read one users info
def one_user(id):
    data = {
        'id': id
    }
    a_user = User.get_one(data)
    return render_template('read_one.html', one_user = a_user)

@app.route('/delete/<int:id>', methods = ["POST"]) #this is to delete user
def delete(id):
    data = {
        'id' : id
    }
    User.delete(data)
    return redirect('/users/new')

@app.route('/edit/<int:id>') #this is the edit page/form
def edit(id):
    data = {
        'id' : id
    }
    a_user = User.get_one(data)
    return render_template('edit.html', one_user = a_user)

@app.route('/update/<int:id>', methods = ['POST']) #this is to actually edit the user
def update(id):
    data = {
        'id' : id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.update(data)
    return redirect(f'/read/{id}') #make sure to add f string - cannot just copy previous link
