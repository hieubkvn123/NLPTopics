import os
import tensorflow as tf

from argparse import ArgumentParser
from tensorflow.keras.models import load_model

from flask import Flask
from flask import request
from flask import render_template
from flask_cors import CORS

### Some prebuilt configurations ###
parser = ArgumentParser()
parser.add_argument('--debug', type=bool, required=False, help='Debug mode on/off')
parser.add_argument('--port', type=int, required=False, help='TCP port to run on')
args = vars(parser.parse_args())

MODELS_DIR = "./models"
WEIGHTS_DIR = "./weights"
PORT = args['port'] if args['port'] else 8080
DEBUG = args['debug'] if args['debug'] else False

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

### Load first model as the default in advance ###
default_model = load_nmt_model(MODELS[0])
print(default_model.summary())

### Start building flask app ###
app = Flask(__name__)
CORS(app)

@app.route("/change_default_model", methods=["POST"])
def change_default_model():
    global default_model

    if(request.method=="POST"):
        try:
            model_name = request.form['model_name']
            default_model = load_nmt_model(model_name)

            print(f'[INFO] Default model changed to {model_name} ...')
            print(default_model.summary())
            return 'success'
        except:
            return 'fail'

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", model_names=MODELS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
