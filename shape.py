class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        print(self.name)
    
class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width
        
    def area(self):
        print(self.length*self.width)
    
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
        
    def area(self):
        print(3.14*(self.radius**2))

rec = Rectangle("rectangle", 4, 8)
o = Circle("circle", 2)

rec.area()
o.area()
