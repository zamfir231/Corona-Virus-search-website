from flask import Blueprint, render_template

#initialize blueprint
view = Blueprint('views', __name__)

# Set up urls
@view.route('/')
def home():
    return render_template('index.html')

@view.route('/coronaVirus')
def coronaVirus():
    return render_template('coronaVirus.html')
