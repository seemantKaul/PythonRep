from FlaskBlog import app
from flask import render_template


@app.route('/')
def home():
    return render_template('index.html', title='Home')


@app.route('/about')
def about():
    return render_template('about.html')
