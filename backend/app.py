from flask import Flask, render_template, request, jsonify
from routes.api import crop_prediction

app = Flask(__name__)

# Import routes
app.register_blueprint(crop_prediction)
# app.register_blueprint(crop_prediction, url_prefix='/predict')

# Home Route
@app.route('/')
def home():
    return render_template('index.html', title = "Home")
    # return render_template('C:\\SoilCropPrediction\\backend\\templates\\index.html')

# about Route
@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/predict')
def predict():
    return render_template("predict.html", title="Predict")

# Contact Route
@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")

if __name__ == '__main__':
    app.run(debug=True)

from routes.views import views
app.register_blueprint(views)


from config.settings import DevelopmentConfig
app.config.from_object(DevelopmentConfig)
