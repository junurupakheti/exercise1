class Holiday:
    def __init__(self, destination=None, duration=0, cost=0):
        self.destination=destination
        self.duration=duration
        self.cost=cost
    def getDestination(self):
        return self.destination
    def getDuration(self):
        return self.duration
    def getCost(self):
        return self.cost
    def set_(self, destination):
        self.destination=destination
    def set_(self, duration):
        self.duration=duration
    def set_(self, cost):
        self.cost=cost
    def __str__(self):
       
       return "Holiday{destination="+str(self.getDestination())+" , duration="+str(self.getDuration())+" days, cost=$"+str(self.getCost())+"}"

#hoily=Holiday("london", 2, 200 )
#print(hoily)
class TravelAgent:
    holidays=[None]
    def __init__(self, name, postcode):
        self. name=name
        self.postcode=postcode
        self.holidays.append(self.name)
        self.holidays.append(self.postcode)
    def getName(self):
        return self.name
    def getPostcode(self):
        return self.postcode
    def set_(self, name):
      self.name=name
    def set_(self, postcode):
        self.postcode=postcode
    def addHoliday(self, holiday = Holiday()):
        self.holidays.append(holiday.__str__())

    def __str__(self):
         return self.holidays.__str__() 

class RunTravelAgent:
    h1 =  Holiday("Bermuda", 2, 800)
    h2 =  Holiday("Hull", 14, 8)
    h3 =  Holiday("Los Angeles", 12, 2100)

    t1 = TravelAgent("CheapAsChips", "MA99 1CU")

    t1.addHoliday(h1)
    t1.addHoliday(h2)
    t1.addHoliday(h3)

    t2 = TravelAgent("Shoe String Tours", "CO33 2DX")

    print(t1)

    print("h3 Duration= "+str(h3.getDuration())+" days & Cost= "+str(h3.getCost()))
    print("t2 "+str(t2.getName())+" "+ str(t2.getPostcode()))
demo=TravelAgent("holly", "cm20 120")
print(demo)