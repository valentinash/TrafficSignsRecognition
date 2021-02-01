from abc import ABC, abstractmethod


class LineDetection(ABC):
    def canny(self, frame):
        """

        :return:
        """
        pass

    def displayLines(self, image, lines):
        """

        :return:
        """
        pass

    def regionOfInterest(self, image):
        """

        :return:
        """
        pass

    @abstractmethod
    def show(self):
        pass