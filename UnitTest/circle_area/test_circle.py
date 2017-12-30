import unittest
from math import pi
from circle import area


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # Test areas when radius >= 0
        self.assertAlmostEqual(area(1), pi)
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(2.1), pi * 2.1**2)

    def test_values(self):
        #Make sure value errors are raised
        self.assertRaises(ValueError, area, -2)

    def test_types(self):
        # Make sure type errors are raised when necessary
        self.assertRaises(TypeError, area, 3 + 5j)
        self.assertRaises(TypeError, area, True)
        self.assertRaises(TypeError, area, "radius")
     
#run from app
if __name__ == '__main__':
  unittest.main()
