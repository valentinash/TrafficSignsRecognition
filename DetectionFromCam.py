from Functions import Methods
from threading import Thread
import cv2
from resources import Constants


class DetectionFromCam(Thread):
    M = Methods()
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()
        redness = M.returnRedness(frame)  # step 1 --> specify the redness of the image
        thresh = M.threshold(redness)
        try:
            contours = M.findContour(thresh)
            big = M.findBiggestContour(contours)
            if cv2.contourArea(big) > 3000:
                print(cv2.contourArea(big))
                img, sign = M.boundaryBox(frame, big)
                cv2.imshow('frame', img)
                print("Shenja e detektuar: ", Constants.labelToText[M.predict(sign)])
            else:
                cv2.imshow('frame', frame)
        except:
            cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
