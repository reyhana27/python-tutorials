class Employee:
    def __init__(self, name):
        self.name = name
        
    def work(self):
        print(self.name)
    
class Developer(Employee):
    def work(self):
        print(self.name)
            
class Designer(Employee):
    def work(self):
        print(self.name)
    
dev = Developer("mike")
des = Designer("emma")
dev.work()
des.work()
    
