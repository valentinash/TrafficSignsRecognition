from abc import ABC, abstractmethod


class LineDetection(ABC):
    @abstractmethod
    def canny(self, frame):
        """
            per indetifikim te skajeve te imazhit """
        pass

    @abstractmethod
    def displayLines(self, image, lines):
        """

        """
        pass
    @abstractmethod
    def regionOfInterest(self, image):
        """
            vizatimi i trekendeshit

        """
        pass

    @abstractmethod
    def show(self):
        pass