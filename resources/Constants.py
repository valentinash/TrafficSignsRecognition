import os
from tensorflow import keras

modelPath = 'models'
model = keras.models.load_model(modelPath + '/TSModel5')

ImagesFilePath = 'ts-scenes/scenes'
ImageNamePath = os.listdir(ImagesFilePath)

labelToText = {0: "Stop",
               1: "Do not Enter",
               2: "Traffic jam is close",
               3: "Yield"}
