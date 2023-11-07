from math import pi

class Circle:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r
    
    def Area(self):
        return pi * self.r ** 2
    
    def Perimeter(self):
        return 2 * pi * self.r
    
    def testBelongs(self, x, y):
        if (x - self.a) ** 2 + (y - self.b) ** 2 == self.r ** 2:
            return f'{x},{y} does belong inside the circle'
        return f'{x},{y} does not belong inside the circle'

C = Circle (1,2,1)

print ("the perimeter of the circle C is:", C.Perimeter() )
print ("the area of circle C is:", C.Area())
print(C.testBelongs(1,1))
