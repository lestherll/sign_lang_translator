import cv2

from pandas import DataFrame
import numpy as np

from keras.models import load_model
from skimage.transform import resize, pyramid_reduce

model = load_model('sign_lang_translator/translator/pre_trained/model.h5')

FONT = cv2.FONT_HERSHEY_SIMPLEX

def prediction(pred):
    return(chr(pred+ 65))

def keras_predict(model, image):
    data = np.asarray( image, dtype="int64" )
    pred_probab = model.predict(data)[0]
    pred_class = list(pred_probab).index(max(pred_probab))
    return max(pred_probab), pred_class


def main():

    c1 = 150
    r1 = 100
    size = 300

    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # crop region of interest
        cropped_img = frame[r1:r1+size, c1:c1+size]
        gray = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)
        blurred_gray = cv2.GaussianBlur(gray, (15,15), 0)
        resized_blurred_gray = cv2.resize(blurred_gray, (28,28), interpolation = cv2.INTER_AREA)
    
        # prepare input for prediction
        inp_layer = np.resize(resized_blurred_gray, (28, 28, 1))
        expanded = np.expand_dims(inp_layer, axis=0)

        # prediction
        pred_probab, pred_class = keras_predict(model, expanded)    
        curr = prediction(pred_class)        
        cv2.putText(frame, curr, (450, 300), FONT, 4.0, (255, 255, 255))
        
        cv2.rectangle(frame, (c1, r1), (c1+size, r1+size), (0, 255, 0), 2)
        cv2.imshow("Video", frame)
        cv2.imshow("ROI", blurred_gray)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
    

if __name__ == '__main__':
    main()

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
