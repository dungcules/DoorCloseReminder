from abc import ABC, abstractmethod

class CamInterface(ABC):
    @abstractmethod
    def connectTo(self):
        pass
    