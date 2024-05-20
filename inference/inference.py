import mlflow
import mlflow.tensorflow
import numpy as np
from tensorflow.keras.models import load_model

def load_model_and_predict(image):
    # Set the MLflow tracking URI
    #mlflow.set_tracking_uri("http://localhost:5000")
    
    # Load the model from the MLflow model registry
    #model = mlflow.tensorflow.load_model("models:/mnist_model/1")  # Version 1
    model=load_model('/app/model/mnist_model.h5')
    print(image)
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    print(image)
    predictions = model.predict(image)
    return np.argmax(predictions[0])

""" if __name__ == "__main__":
    # Example: Load a sample image from the test set
    from load_mnist import load_data
    (_, _), (x_test, y_test) = load_data()
    prediction = load_model_and_predict(x_test[0])
    print(f"Predicted label: {prediction}") """
