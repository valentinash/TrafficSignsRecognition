from resources import Constants
from Functions import Methods
from threading import Thread
import cv2
import numpy as np
from LineDetectionABC import LineDetection


class DetectionFromVideo(LineDetection):
    M = Methods()

    def canny(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('image', gray)# merr dy argumente
        """
        3 Finding Lane Lines
        Gaussian Blur (te hiqen zhurmat e figures)
        """
        blur = cv2.GaussianBlur(gray, (5, 5), 0) #(5,5) - matrice, 0 - devijimi standart
        # cv2.imshow('image', blur)
        """
        3 Finding Lane Lines
        Canny - indetifikimi i skajeve te imazhit
        """
        canny = cv2.Canny(blur, 50, 150)
        # cv2.imshow('image', canny)
        return canny

    def displayLines(self, image, lines):
        lane_image = np.zeros_like(image)
        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line.reshape(4)
                cv2.line(lane_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
        return lane_image

    def regionOfInterest(self, image): #vizatimi i trekendeshit
        height = image.shape[0]
        polygons = np.array([[(200, height), (1100, height), (550, 250)]]) #konturat e poligonit
        mask = np.zeros_like(image) #black image
        cv2.fillPoly(mask, polygons, 255)  #konturat e poligonit ne foto te zeze
        masked_image = cv2.bitwise_and(image, mask) #bitwise_and - merr pikselat nga vendi i pozites
        return masked_image

    """image = cv2.imread('test_image.jpg')
    image = cv2.resize(image, (800, 800))
    lane_image = np.copy(image)
    canny_ = canny(lane_image)
    cropped_image = region_of_interest(canny_)
    lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
    line_image = display_lines(lane_image, lines)
    combo_image = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1)
    cv2.imshow('image', combo_image)
    cv2.waitKey(0) #do ta shfaq foton deri sa ta ndalim ne
    
    """

    def show(self):
        pass

"""
krijohet nje object i klases DetectionFromVideo D
dhe nje object i klases Methods M
"""
D = DetectionFromVideo()
M = Methods()
cap = cv2.VideoCapture('resources/testVideo.mp4')


def detectLines(frame):
    canny_ = D.canny(frame)
    cropped_image = D.regionOfInterest(canny_)
    lines = cv2.HoughLinesP(cropped_image, 2, np.pi / 180, 100, np.array([]), minLineLength=40, maxLineGap=5)
    line_image = D.displayLines(frame, lines)
    combo_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
    cv2.imshow('image', combo_image)


def detectSigns(frame):
    redness = M.redness(frame)  # step 1 --> specify the redness of the image
    thresh = M.threshold(redness)

    contours = M.contour(thresh)
    big = M.biggestContour(contours)
    if cv2.contourArea(big) > 3000:
        print(cv2.contourArea(big))
        img, sign = M.boundaryBox(frame, big)
        #cv2.imshow('frame', img)
        print("Sign:", Constants.labelToText[M.predict(sign)])
    else:
        print("")
        #cv2.imshow('frame', frame)


while cap.isOpened():
    #perderisa video is on play mode
    #lexohen pamjet e videos frame-frame
    _, frame = cap.read()
    """
    krijohen dy threads
    Njeri thread per detektimin e shenjave
    Tjetri thread per detektimin e linjave
    """
    signsThread = Thread(target=detectSigns(frame), args=(frame,))
    linesThread = Thread(target=detectLines(frame), args=(frame,))

    # startohen threadat
    signsThread.start()
    linesThread.start()

    # pritet derisa te kompletohet threadi
    signsThread.join()
    linesThread.join()

    if cv2.waitKey(1) == ord('q'):
        break

cv2.release()
cv2.destroyAllWindows()
