class Car:
    def details(self,brand,mileage,speed):
        self.brand=brand
        self.mileage=mileage
        self.speed=speed
    def transport(self):
        print("used for transport")
    def riding(self):
        print("used for riding")
c1 = Car()
c1.details("Volvo",11,220)
print(c1.speed)