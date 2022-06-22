from django.test import TestCase
from Calculator.models import Operation
# Create your tests here.

class TestOperations(TestCase):
  
    def testMultiplication(self):
        multiplication1=Operation('10','5')
        multiplication1.multiplication()
        self.assertEqual(multiplication1.getResult(),50,"Succès du test!")

        multiplication2=Operation('10a','4')
        multiplication2.multiplication()
        self.assertEqual(multiplication2.getResult(),"Caractère non permis","Succès du test!")

     