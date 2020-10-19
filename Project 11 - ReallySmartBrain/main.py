"""
This module implements the ReallySmartBrain exercise of the Section 21 of the course.
"""

import os
from imageai.Prediction import ImagePrediction


def calculate_prediction():
    # Get te execution path
    execution_path = os.getcwd()

    # Create the image prediction object and load the model
    # See https://github.com/OlafenwaMoses/ImageAI/blob/master/imageai/Prediction/CUSTOMPREDICTION.md#customprediction
    prediction = ImagePrediction()
    prediction.setModelTypeAsSqueezeNet()
    prediction.setModelPath(os.path.join(execution_path, "models/squeezenet_weights_tf_dim_ordering_tf_kernels.h5"))
    prediction.loadModel()

    # Calculate the prediction
    predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "images/giraffe.jpg"),
                                                         result_count=5)

    # Print the results
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction, " : ", eachProbability)


# Entry point of the script
if __name__ == '__main__':
    # Call the calculate prediction function
    calculate_prediction()
