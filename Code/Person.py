# kelas Person merupakan parent dari kelas Driver
class Person:
    # atribut private
    __nik = ""
    __name = ""
    __gender = ""
    
    # contructor
    def __init__(self):
        self.__nik = ""
        self.__name = ""
        self.__gender = ""
    
    # setter and getter of atribute
    def setNik(self, nik):
        self.__nik = nik
    def setName(self, name):
        self.__name = name
    def setGender(self, gender):
        self.__gender = gender
    
    # getter
    def getNik(self):
        return self.__nik
    def getName(self):
        return self.__name
    def getGender(self):
        return self.__gender

    # method untuk sleep()
    def sleep(self, sleepMode):
        if sleepMode == "Sleep":
            print(f"{self.getName()} is sleeping now.")
        else:
            print(f"{self.getName()} is not sleeping now.")
    
    # print method
    def printPerson(self):
        print("NIK           : " + self.getNik())
        print("Name          : " + self.getName())
        print("Gender        : " + self.getGender())