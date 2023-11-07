from math import sqrt

class Geometry:
    def __init__(self):
        pass

    def distance(self, a, b):
        distance = sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
        return distance
    
    def middle(self,a, b):
        x = (a[0] + b[0]) // 2
        y = (a[1] + b[1]) // 2
        return f'The midpoint is ({x},{y})' 

    def trianglePerimeter(self, a, b, c):
        perimeter = a + b + c
        return perimeter
    
    def triangleIsoscel(self, a, b, c):
        if a == b or b == c or a == c:
            return True
        else:
            return False 
    
triangle = Geometry()
print(triangle.distance((9,7),(3,2)))
print(triangle.middle((2,1),(4,3)))
print(triangle.trianglePerimeter(2,3,2))
print(triangle.triangleIsoscel(3,3,2))