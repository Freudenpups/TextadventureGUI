print("Hello World")


class Testen():
    def __init__(self):
        pass
        
    def  addieren(a, b, c):
        b = a + c
        a = b + c
        return a
    
    def starten(self, a, b, c):
        self.addieren(a, b, c)
        
    __repr__:
        return "Testen"
        
        

a = int(input("Waehle Zahl a: "))
b = int(input("Waehle Zahl b: "))
c = int(input("Waehle Zahl c: "))

Testen.addieren(a, b, c)
