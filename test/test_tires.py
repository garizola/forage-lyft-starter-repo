import unittest
from engine.model.tires import CarriganTires, OctoprimeTires


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        wear_values = [0.1, 0.1, 0.9, 0.1]
        tires = CarriganTires(wear_values)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        wear_values = [0.1, 0.1, 0.1, 0.1]
        tires = CarriganTires(wear_values)
        self.assertFalse(tires.needs_service())


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        wear_values = [0.8, 0.8, 0.7, 0.8]
        tires = OctoprimeTires(wear_values)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        wear_values = [0.5, 0.5, 0.5, 0.5]
        tires = OctoprimeTires(wear_values)
        self.assertFalse(tires.needs_service())


if __name__ == '__main__':
    unittest.main()
