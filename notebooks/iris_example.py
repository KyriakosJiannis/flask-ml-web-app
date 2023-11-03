from sklearn.datasets import load_iris
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the Data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=12, test_size=0.20, stratify=y)

# Create the Classifier
model1 = DecisionTreeClassifier(random_state=12)

# Hyperparameter Tuning of DTC
param_grid = {
    'max_depth': [2, 3, 4],
    'min_samples_split': [2, 3, 4],
    'min_samples_leaf': [1, 2, 3, 4, 5],
}

cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=12)
grid_search = GridSearchCV(model1, param_grid, cv=cv, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Passing best parameter for the Hyperparameter Tuning
model1 = grid_search.best_estimator_
model1.fit(X_train, y_train)

# Validate the best model on the test set
y_train_pred = model1.predict(X_train)
print(confusion_matrix(y_train, y_train_pred))

y_pred = model1.predict(X_test)
print(confusion_matrix(y_test, y_pred))

# Save the model as pickle
filename = 'model1.pkl'
pickle.dump(model1, open('models/' + filename, 'wb'))
