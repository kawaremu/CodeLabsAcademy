class Rectangle:
  def __init__(self,length,width) -> None:
    self.length = length
    self.width = width
  
  def get_area(self):
    return self.length*self.width
  
  
rect = Rectangle(5,6)
area = rect.get_area()
print(area)

class Vehicle:
  def __init__(self,max_speed,mileage):
    self.max_speed = max_speed
    self.mileage = mileage
    
    
class VehicleEmpty:
  pass
  
class Bus(Vehicle):
  pass



v = VehicleEmpty()
b = Bus(max_speed=15,mileage=10)
print(b.max_speed)