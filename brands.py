class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        
    def move(self):
        print(self.brand)
    
class Car(Vehicle):
    def move(self):
        print(self.brand)
        
class Bike(Vehicle):
    def move(self):
        print(self.brand)
        
car = Car("toyota")
bike = Bike("yamaha")
car.move()
bike.move()
