from Functions import Methods
from threading import Thread
import cv2
from resources import Constants


class DetectionFromCam(Thread):
    """
    Krijohet nje object i klases Methods
    e cila i permban pothuajse te gjitha funksionet qe perdoren brenda aplikacionit
    """
    M = Methods()

    """
    VideoCapture perdoret edhe per hapje te videos edhe per video permes kameres
    Nese hapet video, si parameter i japim pathin e videos
    Nese hapet kamera, si paramter marrim indexin e pajisjes
    0 - kamera e pare
    1 - kamera e dyte (nese pajisja i ka dy kamera)
    """
    cap = cv2.VideoCapture(0)

    while True:
        """
        Kthen tuple
        Vlera e pare e kthyer eshte e tipit Boolean-nese freame eshte lexuar mire apo jo(True ose False)
        Vlera e dyte e kthyer eshte vete Frame
        """
        _, frame = cap.read()
        redness = M.returnRedness(frame)
        thresh = M.threshold(redness)
        try:
            contours = M.findContour(thresh)
            big = M.findBiggestContour(contours)
            if cv2.contourArea(big) > 3000:
                print(cv2.contourArea(big))
                img, sign = M.boundaryBox(frame, big)
                #shfaq imazhin ne nje dritare
                cv2.imshow('frame', img)
                print("Shenja e detektuar: ", Constants.labelToText[M.predict(sign)])
            else:
                cv2.imshow('frame', frame)
        except:
            cv2.imshow('frame', frame)
        """
        Nese vjen nje komand dhe ajo komande eshte shkronja q
        Atehere do te perfundoj ekzekutim i while loop
        """
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    #lirohet kamera
    cap.release()
    #mbyllen te gjitha dritaret ekzistuese
    cv2.destroyAllWindows()
