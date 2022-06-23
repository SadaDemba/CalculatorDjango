from django.test import TestCase
from Calculator.models import Operation
# Create your tests here.

class TestOperations(TestCase):
  
    def testAddition(self):
        addition1=Operation('10','5')
        addition1.addition()
        self.assertEqual(addition1.getResult(),15,"Succès du test!")

        addition2=Operation('10a','4')
        addition2.addition()
        self.assertEqual(addition2.getResult(),"Désolé! Caractère non permis","Succès du test!")

    def testSoustraction(self):
        soustraction1=Operation('10','5')
        soustraction1.soustraction()
        self.assertEqual(soustraction1.getResult(),5,"Succès du test!")

        soustraction2=Operation('10a','4')
        soustraction2.soustraction()
        self.assertEqual(soustraction2.getResult(),"Caractère non permis","Succès du test!")
    
    
    def testMultiplication(self):
        multiplication1=Operation('10','5')
        multiplication1.multiplication()
        self.assertEqual(multiplication1.getResult(),50,"Succès du test!")

        multiplication2=Operation('10a','4')
        multiplication2.multiplication()
        self.assertEqual(multiplication2.getResult(),"Caractère non permis","Succès du test!")

    def testdivision(self):
        division1=Operation('10','5')
        division1.division()
        self.assertEqual(division1.getResult(),2,"Succès du test!")

        division2=Operation('10','0')
        division2.division()
        self.assertEqual(division2.getResult(),"Impossible de diviser par 0","Succès du test!")

        division3=Operation('10a','4')
        division3.division()
        self.assertEqual(division3.getResult(),"Caractère non permis","Succès du test!")


     