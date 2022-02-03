from django.conf import settings
import numpy as np
import constants


def predict(text):
    prob = settings.MODEL.predict([text], verbose=0).numpy()
    prob = np.max(prob[:, 0])
    return prob > constants.CLASSIFICATION_THRESHOLD
