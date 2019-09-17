import unittest
from my_max import my_max


class TestMaxNumber(unittest.TestCase):

    def test_max_0_and_1(self):
        self.assertEqual(max(0, 1), my_max(0, 1))

    def test_max_3_and_minus5(self):
        self.assertEqual(max(3, -5), my_max(3, -5))
    
    def test_max_6dot7_and_3dot8(self):
        self.assertEqual(max(6.7, 3.8), my_max(6.7, 3.8))

    #def test_max_4_and_tekst(self):
       #self.assertNotEqual(max(4, 'Tekst'), my_max(4, 'Tekst'))


if __name__ == '__main__':
    unittest.main()
