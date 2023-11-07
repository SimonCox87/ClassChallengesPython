class TK:
    def __init__(self, Master, title):
        self.Master = Master
        self.title = title

class TK_extended(TK):
    def __init__(self, Master, title):
        super().__init__(Master, title)
    
    def create(self):
        window = self.title
        return f'Window created titled "{window}"'
    
    def resize(self, specs): #specs is a tuple
        windowSize = specs
        return f'Window Resized.  Width = {windowSize[0]} pixels. Height = {windowSize[1]} pixels.'
    
    def generate(self):
        return "Window is generated."

window = TK_extended("Cheeky App", "Hello")
print(window.create())
print(window.resize((80,100)))
print(window.generate())
