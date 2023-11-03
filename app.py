# app.py

from flask import Flask, render_template, url_for, request
from flask_material import Material
from models.modules import FlowerSpeciesPredictor, ImagePathDeterminer

app = Flask(__name__)
Material(app)
app.config.from_object('config.DevelopmentConfig')


# Initialize the predictor and image path determiner
predictor = FlowerSpeciesPredictor(app.config['MODEL_PATH'])
image_path_determiner = ImagePathDeterminer()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict_result():
    try:
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])

        species = predictor.predict(sepal_length, sepal_width, petal_length, petal_width)
        image_path = image_path_determiner.input(species)

        return render_template('index.html', prediction=species, image_path=image_path)
    except Exception as e:
        return render_template('index.html', error=str(e))


if __name__ == '__main__':
    app.run(port=app.config['PORT'], debug=True)
