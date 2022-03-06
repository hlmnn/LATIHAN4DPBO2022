from Driver import Driver
from Ship import Ship
from Airplane import Airplane

def main():
    # data nik, nama, dan gender
    nik = ["6901", "6902", "6903", "6904", "6905"]
    nama = ["Shigeo Tokuda", "Mario Ozawa", "Johnny Sins", "Fukada Eimi", "Hatano Yui"]
    gender = ["Male", "Female", "Male", "Female", "Female"]
    # data nip, companyName, dan position untuk
    nip = ["4201", "4202", "4203", "4204", "4205"]
    perusahaan = ["Old Chad", "Young Mistress", "Multijob", "Cute Glasses", "IDK"]
    posisi = ["CEO", "Secretary", "Multitalent", "Famous Actress", "Janitor"]
    # data lisenseID, activeUntil, dan vehicleType
    sim = ["4201069", "4202069", "4203069", "4204069", "4205069"]
    masaAktif = ["2066", "2067", "2068", "2069", "2070"]
    tipeKendaraan = ["RX-King", "Supra Bapak", "Speedboat", "Human Carriage", "Slipper"]

    # instansiasi class Driver
    oDriver = [Driver() for i in range(5)]

    # input data Driver
    for i in range(5):
        oDriver[i].setNik(nik[i])
        oDriver[i].setName(nama[i])
        oDriver[i].setGender(gender[i])
        oDriver[i].setNip(nip[i])
        oDriver[i].setCompanyName(perusahaan[i])
        oDriver[i].setposition(posisi[i])
        oDriver[i].setLicenseID(sim[i])
        oDriver[i].setActiveUntil(masaAktif[i])
        oDriver[i].setVehicleType(tipeKendaraan[i])

    # print data Driver nya
    print("===================================")
    print("            Data Person            ")
    print("===================================")
    for i in range(5):
        oDriver[i].printPerson()
        print("------------------------------")

    # print data Driver nya
    print("\n")
    print("===================================")
    print("             Data Job              ")
    print("===================================")
    for i in range(5):
        oDriver[i].printJob()
        print("------------------------------")
    
    # print data Driver nya
    print("\n")
    print("===================================")
    print("            Data Driver            ")
    print("===================================")
    for i in range(5):
        oDriver[i].printDriver()

    # data untuk class Ship
    nameS = ["USS Enterprise", "IJN Yamato", "KMS Bismarck", "IJN Shimakaze", "USS Fletcher"]
    fuelS = ["Deuterium", "Oil", "Oil", "Oil", "Diesel"]
    penumpangS = [5828, 3332, 2200, 267, 329]
    usiaS = [61, 81, 83, 80, 80]
    tipeS = ["Arircraft Carrier", "Battleships", "Battleships", "Destroyer", "Destroyer"]
    produksiS = ["United States", "Japan", "Germany", "Japan", "United States"]

    # instansiasi class Ship
    oShip = [Ship() for i in range(5)]

    # input data Ship
    for i in range(5):
        oShip[i].setName(nameS[i])
        oShip[i].setFuelType(fuelS[i])
        oShip[i].setMaxPassanger(penumpangS[i])
        oShip[i].setAge(usiaS[i])
        oShip[i].setType(tipeS[i])
        oShip[i].setCountryOfManufacture(produksiS[i])

    # print data Ship nya
    print("\n")
    print("==============================================")
    print("                   Data Ship                  ")
    print("==============================================")
    for i in range(5):
        oShip[i].printShip()

    # print data Ship (Vehicle) nya
    print("\n")
    print("==============================================")
    print("                 Data Vehicle                 ")
    print("==============================================")
    for i in range(5):
        oShip[i].printVehicle()
        print("------------------------------")
    
    
    # data untuk class Airplane
    nameA = ["Boeing 747", "Lockheed Martin F-22 Raptor", "Northrop Grumman B-2 Spirit", "Boeing B-52 Stratofortress", "A-10 Thunderbolt II"]
    fuelA = ["Kerosene", "Kerosene", "Kerosene", "Synthetic Fuel", "Hydrogen"]
    penumpangA = [467, 1, 2, 5, 1]
    usiaA = [11, 17, 25, 69, 49]
    tipeA = ["Commercial Aircraft", "Stealth Aircraft", "Stealth Aircraft", "Strategic Bomber", "Attack Aircraft"]
    panjangSayapA = [68, 13.56, 52, 56.4, 17.42]

    # instansiasi class Ship
    oAirplane = [Airplane() for i in range(5)]

    # input data Ship
    for i in range(5):
        oAirplane[i].setName(nameA[i])
        oAirplane[i].setFuelType(fuelA[i])
        oAirplane[i].setMaxPassanger(penumpangA[i])
        oAirplane[i].setAge(usiaA[i])
        oAirplane[i].setType(tipeA[i])
        oAirplane[i].setWingsLength(panjangSayapA[i])

    # print data Airplane nya
    print("\n")
    print("==============================================")
    print("                 Data Airplane                ")
    print("==============================================")
    for i in range(5):
        oAirplane[i].printAirplane()
    
    # print data Airplane (Vehicle) nya
    print("\n")
    print("==============================================")
    print("                 Data Vehicle                 ")
    print("==============================================")
    for i in range(5):
        oAirplane[i].printVehicle()
        print("------------------------------")

if __name__=="__main__":
    main()