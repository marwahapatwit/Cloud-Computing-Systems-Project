import unittest
import lab5

class TestLab5Queries(unittest.TestCase):
    def test_query1(self):
        result = lab5.query1_products_by_price_desc()
        self.assertIsInstance(result, list)

    def test_query2(self):
        result = lab5.query2_customers_full_name()
        self.assertIsInstance(result, list)

    def test_query3(self):
        result = lab5.query3_products_in_price_range()
        self.assertIsInstance(result, list)

    def test_query4(self):
        result = lab5.query4_order_items_with_totals()
        self.assertIsInstance(result, list)

    def test_query5(self):
        result = lab5.query5_join_categories_products()
        self.assertIsInstance(result, list)

    def test_query6(self):
        result = lab5.query6_customer_address_by_email()
        self.assertIsInstance(result, list)

    def test_query7(self):
        result = lab5.query7_shipping_addresses()
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    unittest.main()
