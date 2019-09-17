import unittest
from basicscript import BasicClass

class TestBasicClass(unittest.TestCase):

    def setUp(self):
        self.func = BasicClass()

    def test_initial_state(self):
        self.assertEqual(self.func.state, 0)

    def test_increment(self):
        self.func.increment_state()
        self.assertEqual(self.func.state, 1)

    def test_clear(self):
        self.func.clear_state()
        self.assertEqual(self.func.state, 0)
        
if __name__ == '__main__':
    unittest.main()
