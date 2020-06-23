
def main():
    info=""
    keepGoing=True
    cars=[]
    tolls=[]
    totalTolls=0
    while(keepGoing):
        info=input("Enter type of vehicle(truck/car): ")
        car=TollBooth(info)
        cars.append(car.getVehicle())
        tolls.append(car.getAmount())
        info=input("Would you like to continue?Y/N ")
        info=info.upper()
        totalTolls+=int(car.getAmount())
        if info=="Y":
            keepGoing=True
        else:
            keepGoing=False
    print("VEHICLE\t\tTOLL AMOUNT")
    for i in range(len(cars)):
        print(cars[i]+"\t\t\t$"+str(tolls[i]))

    print()
    print("TOTAL TOLLS: $"+str(totalTolls))


class TollBooth:
    def __init__(self, vehicle=""):
        self._toll=0
        self._vehicle=vehicle
    
    def setVehicle(self, vehicle):
        self._vehicle=vehicle
    
    def getVehicle(self):
        return self._vehicle
    
    def getAmount(self):
        self._vehicle=self._vehicle.lower()
        if self._vehicle=="truck":
            self._toll=2
            return (self._toll)
        else:
            self._toll=1
            return (self._toll)
        
    def __str__(self):
        return self._vehicle+"\t"+str(self._toll)
    

main()