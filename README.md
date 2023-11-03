# Flask ML web app

This Flask web application provides a simple interface using as example Iris dataset
It uses a trained machine learning model to predict the species of an Iris flower.

## Features

- Input fields for sepal length, sepal width, petal length, and petal width.
- Predicts the Iris species based on the provided measurements.
- Displays the predicted species and an image of the corresponding Iris species.

## Prerequisites
1. Clone the Repository: Clone the project repository to your local machine using Git:

```bash
git clone https://github.com/yourusername/flask-ml-web-app
```
2. Navigate to the Project Directory: Move to the project directory:

```bash
cd flask-iris-classification
```
3. Activate your virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```
4. install the required packages
```bash
pip install -r requirements.txt
```

5. Start the Flask application:
```bash
python app.py
```

Open a web browser and go to http://localhost:3000 to use the application.

## Project Structure

The project directory is organized as follows:

    root/
    ├── models/
    │   ├── model1.pkl
    │   └── modules.py
    ├── notebooks/
    │   ├── iris_example.py
    ├── static/
    │   ├── images/
    │   │   ├── error.png
    │   │   ├── Setosa.png
    │   │   ├── Versicolor.png
    │   │   └── Virginica.png
    ├── ├── script.js
    │   └── style.css
    ├── templates/
    │   └── index.html
    ├── .gitgnore
    ├── app.py
    ├── config.py
    ├── LICENSE
    ├── README.md
    └── requirements.txt

    app.py: The main Flask application.
    config.py: Configuration settings for the application.
    models/: Contains the machine learning model and other model-related code.
    notebooks/: Jupyter notebooks used for model training and testing.
    static/: Static assets such as images, styles, and JavaScript files.
    templates/: HTML templates used for rendering the web pages.
 
## Additional Information

- This project uses the Iris dataset from scikit-learn for demonstration purposes.
- The trained model is stored in the models/ directory as model1.pkl.
- Images of Iris species are located in the static/images/ directory.


## License

This project is licensed under the MIT License. See the LICENSE file for details.
Feel free to customize and expand upon this project for your own needs. If you have any questions or need assistance, please don't hesitate to reach out.
Happy coding!

