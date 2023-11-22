import unittest
from rectangle import area, perimeter
class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0, 0)
        self.assertEqual(res, 0)
    def test_area_random_num(self):
        res = area(2,3)
        self.assertEqual(res, 6)
    def test_area_random_float_num(self):
        res = area(2.4,3.6)
        self.assertEqual(res, 8.64)
    def test_area_big_random_num(self):
        res = area(20000, 30000000)
        self.assertEqual(res, 600000000000)

    def test_perimeter_zero(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)
    def test_perimeter_random_num(self):
        res = perimeter(3,2)
        self.assertEqual(res, 10)
    def test_perimeter_random_float_num(self):
        res = perimeter(2.41,3.66)
        self.assertEqual(res, 12.14)
    def test_perimeter_big_random_num(self):
        res = perimeter(20000000, 30000000)
        self.assertEqual(res, 100000000)
    def test_sum_area_perimeter_random_num(self):
        res = area(5, 9) + perimeter(5, 9)
        self.assertEqual(res, 73)
