from Job import Job
from Person import Person
# kelas Driver merupakan child dari kelas Person dan Job
class Driver(Job, Person):
    # atribut private
    __licenseID = ""
    __activeUntil = 0
    __vehicleType = ""

    # constructor
    def __init__(self):
        super().__init__()
        self.__licenseID = ""
        self.__activeUntil = 0
        self.__vehicleType = ""

    # setter
    def setLicenseID(self, licenseId):
        self.__licenseID = licenseId
    def setActiveUntil(self, activeUntil):
        self.__activeUntil = activeUntil
    def setVehicleType(self, vehicleType):
        self.__vehicleType = vehicleType
        
    # getter 
    def getLicenseID(self):
        return self.__licenseID
    def getActiveUntil(self):
        return self.__activeUntil
    def getVehicleType(self):
        return self.__vehicleType

    # print data
    def printDriver(self):
        self.printPerson()
        self.printJob()
        print("Lisense ID    : " + self.getLicenseID())
        print("Active Untill : " + self.getActiveUntil())
        print("Vehicle Type  : " + self.getVehicleType())
        self.sleep("Sleep")
        print("----------------------------------")