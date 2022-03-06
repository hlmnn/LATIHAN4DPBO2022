# kelas Job merupakan parent dari kelas Driver
class Job:
    # atribut private
    __nip = ""
    __companyName = ""
    __position = ""

    # constructor
    def __init__(self):
        self.__nip = ""
        self.__companyName = ""
        self.__position = ""
    
    # setter
    def setNip(self, nip):
        self.__nip = nip
    def setCompanyName(self, companyName):
        self.__companyName = companyName
    def setposition(self,position):
        self.__position = position

    # getter 
    def getNip(self):
        return self.__nip
    def getCompanyName(self):
        return self.__companyName
    def getPosition(self):
        return self.__position

    # method untuk print
    def printJob(self):
        print("NIP           : " + self.getNip())
        print("Company Name  : " + self.getCompanyName())
        print("Position      : " + self.getPosition())