import unittest
import math
from circle import circle_area, circle_perimeter
from rectangle import rectangle_area, rectangle_perimeter
from triangle import triangle_area, triangle_perimeter

class TestCircle(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(1), math.pi)
        self.assertAlmostEqual(circle_area(3), math.pi * 9)

    def test_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(0), 0)
        self.assertAlmostEqual(circle_perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(circle_perimeter(3), 2 * math.pi * 3)


class TestRectangle(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(0, 5), 0)
        self.assertEqual(rectangle_area(4, 0), 0)
        self.assertEqual(rectangle_area(4, 5), 20)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle_perimeter(4, 5), 18)
        self.assertEqual(rectangle_perimeter(0, 5), 10)
        self.assertEqual(rectangle_perimeter(4, 0), 8)


class TestTriangle(unittest.TestCase):
    def test_triangle_area(self):
        self.assertEqual(triangle_area(0, 5), 0)
        self.assertEqual(triangle_area(4, 0), 0)
        self.assertEqual(triangle_area(6, 4), 12)

    def test_triangle_perimeter(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)
        self.assertEqual(triangle_perimeter(0, 4, 5), 9)
        self.assertEqual(triangle_perimeter(3, 0, 5), 8)

if __name__ == "__main__":
    unittest.main()
