import unittest

from food_ordering_solution import FoodOrderingSolution

class DummyHelper:
    def println(self, msg):
        pass  # For compatibility, does nothing

class TestFoodOrderingSolution(unittest.TestCase):
    def setUp(self):
        self.solution = FoodOrderingSolution()
        self.solution.init(DummyHelper())

    def test_order_and_rate(self):
        # Place orders
        self.solution.order_food("o1", "r1", "f1")
        self.solution.order_food("o2", "r2", "f1")
        self.solution.order_food("o3", "r1", "f2")
        self.solution.order_food("o4", "r3", "f1")

        # Rate orders
        self.solution.rate_order("o1", 5)
        self.solution.rate_order("o2", 4)
        self.solution.rate_order("o3", 3)
        self.solution.rate_order("o4", 5)

        # Test top rated restaurants overall
        top_restaurants = self.solution.get_top_rated_restaurants()
        self.assertEqual(top_restaurants[0], "r3")
        self.assertIn("r2", top_restaurants)
        self.assertIn("r3", top_restaurants)

        # Test top restaurants by food
        top_by_food_f1 = self.solution.get_top_restaurants_by_food("f1")
        self.assertEqual(top_by_food_f1[0], "r1")
        self.assertIn("r2", top_by_food_f1)
        self.assertIn("r3", top_by_food_f1)

        top_by_food_f2 = self.solution.get_top_restaurants_by_food("f2")
        self.assertEqual(top_by_food_f2[0], "r1")

    # def test_no_ratings(self):
    #     self.solution.order_food("o1", "r1", "f1")
    #     self.solution.order_food("o2", "r2", "f1")
    #     # No ratings yet
    #     self.assertEqual(self.solution.get_top_rated_restaurants(), ["r1", "r2"])
    #     self.assertEqual(self.solution.get_top_restaurants_by_food("f1"), ["r1", "r2"])
    #
    # def test_multiple_ratings(self):
    #     self.solution.order_food("o1", "r1", "f1")
    #     self.solution.order_food("o2", "r1", "f1")
    #     self.solution.rate_order("o1", 5)
    #     self.solution.rate_order("o2", 3)
    #     top_restaurants = self.solution.get_top_rated_restaurants()
    #     self.assertEqual(top_restaurants[0], "r1")
    #     top_by_food = self.solution.get_top_restaurants_by_food("f1")
    #     self.assertEqual(top_by_food[0], "r1")

if __name__ == "__main__":
    unittest.main()