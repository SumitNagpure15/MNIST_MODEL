from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
import io
from inference import load_model_and_predict
 
app = Flask(__name__)
 
@app.route('/predict', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image file in request"}), 400
 
    file = request.files['image']
 
    try:
        image = Image.open(file.stream)
        image = image.convert('L')
        image = image.resize((28, 28), Image.ANTIALIAS)
        image_array = np.array(image).astype(float)
 
        print(image_array)
        pred_label = load_model_and_predict(image_array)

        print("Preiction done")
        response = {
            "message": "Prediction done",
            "prediction": str(pred_label)
        }
        return jsonify(response)
 
    except Exception as e:
        return jsonify({"error": str(e)}), 500
 
#if __name__ == '__main__':
#    app.run(debug=True, port=5000)