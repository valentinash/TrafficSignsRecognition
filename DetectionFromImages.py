import time
import numpy as np
from Functions import Methods
import cv2
from resources import Constants


class DetectionFromImages(Methods):
    M = Methods()
    if __name__ == '__main__':
        for i in Constants.ImageNamePath:
            testCase = M.readImage(i)
            img = np.copy(testCase)
            try:
                img = M.filteringImages(img)
                img = M.returnRedness(img)
                img = M.threshold(img, T=155)
                img = M.morphology(img, 11)
                contours = M.findContour(img)
                big = M.findBiggestContour(contours)
                testCase, sign = M.boundaryBox(testCase, big)
                #merr kohen ne miliskonda
                tic = time.time()
                print("Shenja e detektuar: ", Constants.labelToText[M.predict(sign)])
                #toc = time.time()
                #print("Running Time of Model4", (toc - tic) * 1000, 'ms')
                print("--------------------------------------------------------")
                if cv2.waitKey(1) == ord('q'):
                    break
            except:
                pass
            M.show(testCase)
            M.show(img)
