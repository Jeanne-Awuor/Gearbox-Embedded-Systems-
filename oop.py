import math
class circle:
    def __init__(self,diameter):
        self.diameter = diameter
    def areacircle(self):
        radius = self.diameter/2
        areacircle= math.pi* radius**2
        return areacircle
    
class rectangle:
    def __init__(self,length,width) :
        self.length = length
        self.width = width
    def arearectangle(self):
        arearectangle = self.length * self.width
        return arearectangle

class square:
    def __init__(self,side):
        self.side = side
    def areasquare(self):
        areasquare = self.side*self.side
        return areasquare

class righttriangle:
    def __init__(self,base,height) :
        self.base = base
        self.height = height
    def arearighttriangle(self):
        arearighttriangle = 0.5*self.base*self.height
        return arearighttriangle
    
diameter = float(input("Enter the diameter:"))  
c1=circle(diameter)
print("Area of the circle is", c1.areacircle())

r1=rectangle(5,10)
print("Area of rectangle with width 10 and length 5:",r1.arearectangle())

s1=square(3)
print("Area of a square with side 3 units:",s1.areasquare())
 
rr1=righttriangle(5,10)
print("area of a right angled triangle with base 5 and height 10:",rr1.arearighttriangle())