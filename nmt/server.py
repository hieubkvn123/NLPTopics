import os
import tensorflow as tf

from tensorflow.keras.models import load_model

from flask import Flask
from flask import request
from flask import render_template
from flask_cores import CORS

MODELS_DIR = "./models"
WEIGHTS_DIR = "./weights"
PORT = 8080
DEBUG = False

MODELS = [
    "rnn_model",
    "rnn_with_embedding_model",
    "birnn_with_embedding_model"
]

def load_nmt_model(model_name):
    model_file = f'{MODELS_DIR}/{model_name}.h5'
    weights_file = f'{WEIGHTS_DIR}/{model_name}.weights.hdf5'

    model = load_model(model_file)
    model.load_weights(weights_file)

    return model

### Start building flask app ###
app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
