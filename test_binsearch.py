import numpy as np
import unittest

from binarysearch import binary_search

class MyTest(unittest.TestCase):
    
    def test_binsearch(self):
        input = list(range(10))
        self.assertEqual(binary_search(input,5), 5)

    def test_Nan(self):
        input = [np.nan]*5
        with self.assertRaises(TypeError):
            binary_search(input,2)

    def test_type_dismatch(self):
        input=['a']*5
        with self.assertRaises(TypeError):
            binary_search(input,3)

    def test_input_not_sequence(self):
        input = set([1,2,3,4,5])
        with self.assertRaises(TypeError):
            binary_search(input, 3)

    def test_inf(self):
        input = [1, 2, np.inf]
        self.assertEqual(binary_search(input, np.inf), 2)

    def test_empty(self):
        self.assertEqual(binary_search([],1),-1)
        
    def test_boundary(self):
        input = list(range(10))
        self.assertEqual(binary_search(input,1,3,1),-1)

    def test_item_in_array(self):
        input = list(range(10))
        self.assertEqual(binary_search(input,11),-1)
        self.assertEqual(binary_search(input,-1),-1)

    def test_extremes(self):
        input = list(range(10))
        self.assertEqual(binary_search(input,9),9)
        self.assertEqual(binary_search(input,0),0)

    def test_return_first(self):
        input = [3]*10
        self.assertEqual(binary_search(input,3),0)

    def test_overflow(self):
        input = list(range(10))
        self.assertEqual(binary_search(input,np.inf+1),-1)

        
if __name__ == '__main__':
    unittest.main()
    
    