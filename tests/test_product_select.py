from src.vending_features.product_select import ProductSelect
import unittest

class ProductSelectTest(unittest.TestCase):
    def setUp(self):
        self.product_select = ProductSelect()

    def test_select_product(self):
        self.product_select.select_product('cola')
        self.assertEqual(self.product_select.product_selected, 'cola')
        self.assertEqual(self.product_select.price_needed, 100)

    def test_deselect_product(self):
        self.product_select.select_product('cola')
        self.product_select.deselect_product()
        self.assertEqual(self.product_select.product_selected, None)
        self.assertEqual(self.product_select.price_needed, 0)