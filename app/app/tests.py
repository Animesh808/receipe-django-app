from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):

    def test_add(self):
        res = calc.add(3, 9)
        self.assertEqual(res, 12)

    def test_subtract_numbers(self):
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)
