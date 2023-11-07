class str:
    stack = []
    def __init__(self):
        pass
        
    def append(self,text):
        self.text = text
        str.stack.append(self.text)
    
    def pop(self):
        str.stack.pop()
        return self.text

class myString(str):
    def __init__(self):
        str.__init__(self)


stacky = myString()
stacky.append("Hello")
stacky.append("world")
stacky.append("!")
print(stacky.pop())
