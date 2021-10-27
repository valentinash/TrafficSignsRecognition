import cv2
import numpy as np
from resources import Constants


class Methods:

    def redness(self, img):
        yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        y, u, v = cv2.split(yuv)
        return v

    def threshold(self, img, T=150):
        _, img = cv2.threshold(img, T, 255, cv2.THRESH_BINARY)
        return img

    def contour(self, img):
        contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return contours

    def biggestContour(self, contours):
        m = 0
        c = [cv2.contourArea(i) for i in contours]
        return contours[c.index(max(c))]

    def boundaryBox(self, img, contours):
        x, y, w, h = cv2.boundingRect(contours)
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        sign = img[y:(y + h), x:(x + w)]
        return img, sign

    def preprocessingImageToClassifier(self, image=None, imageSize=28, mu=89.77428691773054, std=70.85156431910688):
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        image = cv2.resize(image, (imageSize, imageSize))
        image = (image - mu) / std
        image = image.reshape(1, imageSize, imageSize, 1)
        return image

    def predict(self, sign):
        img = self.preprocessingImageToClassifier(sign, imageSize=28)
        return np.argmax(Constants.model.predict(img))

    def predict3(self, sign):
        img = self.preprocessingImageToClassifier(sign, imageSize=32)
        return np.argmax(Constants.model.predict(img))

    def readImage(self, imagePath):
        img = cv2.imread(Constants.ImagesFilePath + '/' + imagePath, 1)
        img = cv2.resize(img, (500, 400))
        return img

    def increaseContrast(self, img, alpha, beta):
        img = cv2.addWeighted(img, alpha, np.zeros(img.shape, img.dtype), 0, beta)
        return img

    def filteringImages(self, img):
        img = cv2.GaussianBlur(img, (11, 11), 0)
        return img

    def show(self, img):
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def morphology(self, img, kernelSize=7):
        kernel = np.ones((kernelSize, kernelSize), np.uint8)
        opening = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
        return opening
