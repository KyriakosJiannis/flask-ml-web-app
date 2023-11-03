import numpy as np
import pickle


class FlowerSpeciesPredictor:
    def __init__(self, model_path):
        """
        Initialize the iris species with a machine learning model.

        :param model_path:
        """
        # Load the machine learning model during class initialization
        self.loaded_model = pickle.load(open(model_path, 'rb'))

    def predict(self, sepal_length, sepal_width, petal_length, petal_width):
        """
        Predict the species of an Iris flower based on its characteristics.

        :param sepal_length: float
            The length of the sepal in centimeters
        :param sepal_width: float
            The width of the sepal in centimeters
        :param petal_length: float
            The length of the petal in centimeters
        :param petal_width: float
            The width of the petal in centimeters

        :return: str
            The predicted species of the Iris flower.
        """
        # Prepare input data for prediction and make them
        input_data = np.array([sepal_length, sepal_width, petal_length, petal_width]).reshape(1, -1)
        result = self.loaded_model.predict(input_data)

        # Map the result label to a class name
        return self._map_label_to_class(result[0])

    @staticmethod
    def _map_label_to_class(label):
        # Define a mapping of numerical labels to class names
        label_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}

        # Use the mapping to get the corresponding class name
        return label_map.get(label, 'unknown')


class ImagePathDeterminer:
    def __init__(self):
        """
        Initialize the Image Path with for species.
        """
        # Define a mapping of species to image paths
        self.image_mapping = {
            'setosa': 'static/images/Setosa.png',
            'versicolor': 'static/images/Versicolor.png',
            'virginica': 'static/images/Virginica.png',
        }

        # Define a default image path
        self.default_image = 'static/images/error.png'

    def input(self, species):
        """
        Determine the image path based on the predicted species, default to the error image.

        :param species: str
            The predicted species of the Iris flower.
        :return: str
            The image path associated with the predicted species.
        """
        return self.image_mapping.get(species, self.default_image)
