import tensorflow as tf
import numpy as np           
import cv2                                 

def recognize_scene(image):

    if len(image.shape) > 2 and image.shape[2] == 4:
    	image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
 
    image = cv2.resize(image, (256,256))
    
    image = np.array(image, dtype = 'float32')
    image = image / 255.0
    image = np.expand_dims(image, axis=0)

    model = tf.keras.models.load_model("VGG16_16_epochs_256_imres_Model.h5")
    prediction = np.argmax(model.predict(image))
    classes_dict = {0: 'airport_inside', 1: 'bakery', 2: 'bedroom', 3: 'greenhouse', 4: 'gym', 5: 'kitchen', 6: 'operating_room', 7: 'poolinside', 8: 'restaurant', 9: 'toystore'}
    return classes_dict[prediction]

    
