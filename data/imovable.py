from abc import ABC


class TankOperationsIMovable(ABC):

    def getPosition(self):
        pass

    def setPosition(self, value):
        pass

    def getVelocity(self):
        pass
