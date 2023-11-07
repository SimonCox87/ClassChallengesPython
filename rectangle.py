class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def Perimeter(self):
        perimeter = (self.length + self.width) *2
        return perimeter
        
    
    def Area(self):
        area = self.length * self.width
        return area


    def Display(self):
        return f'The length of the Rectangle is: {self.length} \nThe width of the Rectangle is: {self.width} \nThe area of the Rectangle is: {self.Area()} \nThe perimeter of the Rectangle is: {self.Perimeter()}'

class Triangle(Rectangle):
    pass
    
    def area(self):
        area = super().Area() / 2
        return area
    
    def Display(self):
        return f'The area of the Triangle is: {self.area()}'

rectangle = Rectangle(2,5)
print(rectangle.Display())
triangle = Triangle(2,5)
print(triangle.Display())


