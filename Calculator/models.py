from django.db import models

# Create your models here.
class Operation:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        self.res=0

    def setResult(self,result):
        self.res=result

    def getResult(self):
        return self.res
    
    
    def addition(self):
        if self.num1.isnumeric() and self.num2.isnumeric():
            a = int(self.num1)
            b = int(self.num2)
            c = a+b
            self.setResult(c)
        else:
            self.setResult("Désolé! Caractère non permis")

    def soustraction(self):
        if self.num1.isnumeric() and self.num2.isnumeric():
            a = int(self.num1)
            b = int(self.num2)
            c = a-b
            self.setResult(c)
        else:
            self.setResult("Caractère non permis")
    
    def multiplication(self):
        if self.num1.isnumeric() and self.num2.isnumeric():
            a = int(self.num1)
            b = int(self.num2)
            c = a*b
            self.setResult(c)
        else:
            self.setResult("Caractère non permis")

    def division(self):
        if self.num1.isnumeric() and self.num2.isnumeric():
            a = int(self.num1)
            b = int(self.num2)
            if b == 0:
                self.setResult("Impossible de diviser par 0")
            else:
                c = a / b
                self.setResult(c)
        else:
            self.setResult("Caractère non permis")
