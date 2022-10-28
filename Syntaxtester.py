import unittest
from main import *

class First_test(unittest.TestCase):
    def first_test_sample_input_1(self):
        self.assertEqual(kolla_molekyl("Na"), "Formeln är syntaktiskt korrekt")

    def first_test_sample_input_2(self):
        self.assertEqual(kolla_molekyl("H2O"), "Formeln är syntaktiskt korrekt")

    def first_test_sample_input_3(self):
        self.assertEqual(kolla_molekyl("Si(C3(COOH)2)4(H2O)7"), "Formeln är syntaktiskt korrekt")

    def first_test_sample_input_4(self):
        self.assertEqual(kolla_molekyl("Na332"), "Formeln är syntaktiskt korrekt")


class Second_test(unittest.TestCase):
    def second_test_sample_input_1(self):
        self.assertEqual(kolla_molekyl("C(Xx4)5"), "Okänd atom vid radslutet 4)5")

    def second_test_sample_input_2(self):
        self.assertEqual(kolla_molekyl("C(OH4)C"), "Saknad siffra vid radslutet C")

    def second_test_sample_input_3(self):
        self.assertEqual(kolla_molekyl("C(OH4C"), "Saknad högerparentes vid radslutet")

    def second_test_sample_input_4(self):
        self.assertEqual(kolla_molekyl("H2O)Fe"), "Felaktig gruppstart vid radslutet )Fe")

    def second_test_sample_input_5(self):
        self.assertEqual(kolla_molekyl("H0"), "För litet tal vid radslutet")

    def second_test_sample_input_6(self):
        self.assertEqual(kolla_molekyl("H1C"), "För litet tal vid radslutet C")

    def second_test_sample_input_7(self):
        self.assertEqual(kolla_molekyl("H02C"), "För litet tal vid radslutet 2C")

    def second_test_sample_input_8(self):
        self.assertEqual(kolla_molekyl("Nacl"), "Saknad stor bokstav vid radslutet cl")

    def second_test_sample_input_9(self):
        self.assertEqual(kolla_molekyl("a"), "Saknad stor bokstav vid radslutet a")

    def second_test_sample_input_10(self):
        self.assertEqual(kolla_molekyl("(Cl)2)3"), "Felaktig gruppstart vid radslutet )3")

    def second_test_sample_input_11(self):
        self.assertEqual(kolla_molekyl(")"), "Felaktig gruppstart vid radslutet )")


    def second_test_sample_input_12(self):
        self.assertEqual(kolla_molekyl("2"), "Felaktig gruppstart vid radslutet 2")


if __name__ == '__main__':
    unittest.main()

