import unittest
from opdrachtboete import boete


class TestMaxSpeed(unittest.TestCase):

    def test_max_45_and_50(self):
        self.assertEqual(boete(45), 'oke')

    def test_max_50_and_plus5(self):
        self.assertGreater(max(50, +5), speed(3, -5))
    
    def test_max_50_and_65(self):
        self.assertGreaterEqual(max(65, 50), speed(65, 50))

    def test_max_50_and_90(self):
        self.assertGreaterEqual(max(90, 50), speed (90, 50))

    #def test_max_4_and_tekst(self):
       #self.assertNotEqual(max(4, 'Tekst'), my_max(4, 'Tekst'))


if __name__ == '__main__' :
    unittest.main()