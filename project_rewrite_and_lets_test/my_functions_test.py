import unittest
import my_functions


class TestMyFunctions(unittest.TestCase):

    def test_min(self):
        self.assertEqual(my_functions.min(3, 7), 3)
    
    def test_max(self):
        self.assertEqual(my_functions.max([19, 72, 0, -89, 78, 3, 6]), 78)
    
    def test_lenght(self):
        self.assertEqual(my_functions.len([19, 72, 0, -89, 78, 3, 6]), 7)

 
if __name__ == '__main__':
    unittest.main()
