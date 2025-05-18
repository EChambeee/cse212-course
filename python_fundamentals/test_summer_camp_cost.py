import unittest
from summer_camp_cost import calculate_camp_price

class TestSummerCampCost(unittest.TestCase):
    def test_low_income_three_children(self):
        result = calculate_camp_price(age=9, children=3, income=20000)
        expected = 1000 * (1 - 0.90)  # 1000 base price, 90% discount
        self.assertEqual(result, expected)

    def test_high_income(self):
        result = calculate_camp_price(age=14, children=2, income=80000)
        expected = 2000  # No discount
        self.assertEqual(result, expected)

    def test_too_young(self):
        result = calculate_camp_price(age=6, children=2, income=30000)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
