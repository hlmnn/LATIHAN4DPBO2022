# kelas Driver merupakan parent dari kelas Ship dan Airplane
class Vehicle:
    # atribut private
    __name = ""
    __fuelType = ""
    __maxPassenger = 0

    # constructor
    def __init__(self):
        self.__name = ""
        self.__fuelType = ""
        self.__maxPassenger = 0
    
    # setter
    def setName(self, name):
        self.__name = name
    def setFuelType(self, fuelType):
        self.__fuelType = fuelType
    def setMaxPassanger(self, maxPassenger):
        self.__maxPassenger = maxPassenger
    
    # getter
    def getName(self):
        return self.__name
    def getFuelType(self):
        return self.__fuelType
    def getMaxPassanger(self):
        return self.__maxPassenger

    def move(self, moveMode):
        if moveMode == "Move":
            print(self.getName() + " is moving now.")
        else:
            print(self.getName() + " is not moving now.")
    
    # print data
    def printVehicle(self):
        print("Name                   : " + self.getName())
        print("Fuel Type              : " + self.getFuelType())
        print("Max Passanger          : " + str(self.getMaxPassanger()))