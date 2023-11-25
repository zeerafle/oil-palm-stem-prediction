import numpy as np
import tensorflow as tf
from joblib import load
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array

resnet = ResNet50(weights='imagenet', include_top=False)
avg = tf.keras.layers.GlobalAveragePooling2D()(resnet.output)
deep_feature_extractor = tf.keras.Model(inputs=resnet.input, outputs=avg)
model = load('static/model/pipeline_224_globalavgpool.joblib')


def extract_feature(image) -> np.ndarray:
    """Extract feature from image."""
    image = preprocess_input(img_to_array(image))
    feature_maps = deep_feature_extractor.predict(np.array([image]))
    return feature_maps


def predict(image_path) -> str:
    """
    Predict the image.
    :param image: batch of images
    :return: str, prediction result
    """
    # load image
    image = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))

    # extract image feature
    extracted_feature = extract_feature(image)
    print(extracted_feature.shape)

    # make prediction
    prediction = model.predict(extracted_feature)
    print(prediction)

    # decode prediction result
    # normal if the result 0, otherwise infected
    return 'Normal' if not prediction else 'Infected'
