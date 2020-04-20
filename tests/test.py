import unittest
from heat_index import calculate


class TestCalculateMethods(unittest.TestCase):

    def test_celsius(self):
        self.assertEqual(
            round(calculate.from_celsius(
                28, 60
            ), 2), 30.01)
        self.assertEqual(
            round(calculate.from_celsius(
                28, 40
            ), 2), 27.3)

    def test_fahrenheit(self):
        self.assertEqual(
            round(calculate.from_fahrenheit(
                82, 60
            ), 2), 85.3)
        self.assertEqual(
            round(calculate.from_fahrenheit(
                82, 40
            ), 2), 80.64)


if __name__ == '__main__':
    unittest.main()
