# backend/routes/views.py
from flask import Blueprint, render_template

# Blueprint for views
views = Blueprint('views', __name__)

# Route for homepage
@views.route('/')
def home():
    return render_template('index.html')
