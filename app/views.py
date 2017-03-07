"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash
import smtplib

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/profile',methods=["POST","GET"])
def profile():
    """Render the website contact page"""
    if request.method=="POST":
        fname=request.form['name']
        lname=request.form['lname']
        age=request.form['age']
        gender=request.form['gender']
        message=request.form['message']
        picture=request.form['picture']
        send_email(name,email,subject,message)
        flash('Information recorded successfully','success')
        return redirect(url_for('home'))
    return render_template('profile.html')

@app.route('/profiles',methods=["GET"])
def profiles():
    """Render the website's list all profiles page."""
    return render_template('profiles.html')

@app.route('/profile/<userid>', methods=["GET"])
def userid():
    """Render the website's find user page."""
    return render_template('userid.html')
        
def send_email(from_name, from_email, subject, msg):
    from_addr= ''
    to_addr = ''
    message= """
    From: {} <{}>
    To: {}<{}>
    subject: {}
    {}
    """
    to_name="jay"
    
    message_to_send = message.format(from_name, from_addr,to_name, to_addr, subject,msg)
    username=''
    password=''
    server= smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(from_addr,to_addr,message_to_send)
    server.quit()    


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