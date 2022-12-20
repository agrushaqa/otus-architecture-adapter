from data.imovable import TankOperationsIMovable


class AutoGeneratedMovableAdapter(TankOperationsIMovable):
    def __init__(self, obj, ioc):
        self.obj = obj
        self.ioc = ioc

    def getPosition(self):
        self.ioc.resolve(TankOperationsIMovable.getPosition, self.obj
                         ).execute()

    def getVelocity(self):
        self.ioc.resolve(TankOperationsIMovable.getVelocity, self.obj
                         ).execute()

    def setPosition(self, value):
        self.ioc.resolve(TankOperationsIMovable.setPosition, self.obj
                         ).execute()
