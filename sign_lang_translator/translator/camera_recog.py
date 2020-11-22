import cv2

from pandas import DataFrame

from keras.models import load_model
from skimage.transform import resize, pyramid_reduce

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

        # mirror
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # crop region of interest
        img = frame[r1:r1+size, c1:c1+size]

        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.rectangle(frame, (c1, r1), (c1+size, r1+size), (0, 255, 0), 2)

        cv2.imshow("Video", frame)
        cv2.imshow("ROI", img)

        img = cv2.resize(img, (28, 28))
        img = img.reshape(1, 784)
        df = DataFrame(data=img)
        df = df.values
        df = df/255
        df = df.reshape(-1,28,28,1)

        # print(df)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            # print(df.shape)
            # df.to_csv("file.csv")
            #sleep(2)
            break
    

if __name__ == '__main__':
    main()

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
