import cv2

from pandas import DataFrame

font = cv2.FONT_HERSHEY_SIMPLEX

# faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # mirror
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # facial recognition
    # faces = faceCascade.detectMultiScale(
    #     frame,
    #     scaleFactor=1.1,
    #     minNeighbors=5,
    #     minSize=(30, 30),
    #     flags=cv2.CASCADE_SCALE_IMAGE
    # )

    # ROI
    c1 = 150
    r1 = 100
    size = 300

    # crop region of interest
    img = frame[r1:r1+size, c1:c1+size]
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.rectangle(frame, (c1, r1), (c1+size, r1+size), (0, 255, 0), 2)

    # Draw a rectangle around the faces
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # draw text
    # cv2.putText(frame, "HEY", (10,450), font, 3, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow("Video", frame)
    #cv2.imshow("gray", gray)
    cv2.imshow("ROI", img)

    img = cv2.resize(img, (28, 28))
    df = DataFrame(data=img)
    # df = df.values
    # df = df.reshape(-1, 28, 28, 1)

    print(df)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        
        # DataFrame(df).to_csv("file1.csv", index=True, index_label="pixel")
        # df.to_csv("file1.csv", index=True, index_label="pixel")
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
