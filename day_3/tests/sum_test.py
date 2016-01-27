import unittest
from source.my_sum import my_sum

class SumTest(unittest.TestCase):

    def test_two_integers(self):
        result = my_sum(10, 10)
        self.assertEqual(20, result)
