import unittest
from opdrachtboete import boete


class speed(unittest.TestCase):

    def test_max_45_and_50(self):
        self.assertEqual(boete(45), 'oke')

    def test_max_50_and_65(self):
        self.assertNotEqual(boete(65), '€30 boete')
    

    #def test_max_4_and_tekst(self):
       #self.assertNotEqual(max(4, 'Tekst'), my_max(4, 'Tekst'))


if __name__ == '__main__' :
    unittest.main()