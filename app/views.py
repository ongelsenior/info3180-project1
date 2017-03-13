"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash,jsonify
from models import UserProfile
from forms import ProfileForm
import math
from app import db
from werkzeug import secure_filename
from datetime import date, datetime
from time import strftime
import random

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/profile',methods=["POST","GET"])
def profile():
    """Create a profile"""
    form = ProfileForm()
    if request.method=="POST":
        username = request.form ['username']
        id = random.randint(1000000, 1099999)
        fname=request.form['fname']
        lname=request.form['lname']
        age=request.form['age']
        gender=request.form['gender']
        message=request.form['message']

        file = request.files['picture']
        picture = secure_filename(file.filename)
        file.save(os.path.join("app/static/images", picture))
     
        datejoined= datetime.now().strftime("%a, %d %b %Y")

        profile = UserProfile (userid, username, fname, lname, age, message, gender, picture, datejoined)
        db.session.add(profile)
        db.session.commit()
        
        flash('Information recorded '+username,'success')
        return redirect(url_for('home'))
    return render_template('profile.html')

@app.route('/profiles',methods=["POST","GET"])
def profiles():
    """Render the website's list all profiles page."""
    users = db.session.query(UserProfile).all()
    if request.headers['Content-Type']=='application/json' or request.method == "POST":
        ulist=[]
        for user in users:
            ulist.append({'userid':user.id, 'username':user.username})
            users = {'users': ulist}
        return jsonify(users)
                
    return render_template('profiles.html', users=users)

@app.route('/profile/<userid>', methods=["POST","GET"])
def userid(userid):
    """Render the website's find a user's page."""
    users = UserProfile.query.filter_by(userid=userid).first()
    iURL = url_for('static', filename='images/' +users.picture) 

    if request.headers['Content-Type']=='application/json' or request.method == "POST":
        return jsonify(userid=users.userid, username=users.username, picture=users.picture, gender=users.gender, age=users.age, datejoined=users.datejoined)
        
    else:
        
        userp = {'userid':users.id, 'username':users.username, 'picture':iURL, 'age':users.age, 'fname':users.fname, 'lname':users.lname, 'gender':users.gender, 'message':users.message, 'date joined':users.datejoined}
        return render_template('userid.html', userp=userp)



###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")