import tensorflow as tf
import mlflow
import mlflow.tensorflow
from load_mnist import load_data

def build_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

if __name__ == "__main__":
    # Set the tracking URI programmatically
    #mlflow.set_tracking_uri("http://localhost:4000")

    (x_train, y_train), (x_test, y_test) = load_data()
    model = build_model()
    
    # Start an MLflow run
    with mlflow.start_run() as run:
        mlflow.tensorflow.autolog()
        
        # Train the model
        model.fit(x_train, y_train, epochs=5)
        
        # Save the model locally
        model.save('mnist_model.h5')
        
        # Log the model explicitly (Optional, as autolog should handle it)
        #mlflow.tensorflow.log_model(model, "mnist_model")

        # Register the model
        #model_uri = f"runs:/{run.info.run_id}/mnist_model"
        #mlflow.register_model(model_uri, "mnist_model")

        print(f"Model logged in run: {run.info.run_id}")

    print("Model trained, logged, and registered successfully.")
