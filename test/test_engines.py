import unittest
from datetime import datetime
from engine.model.engines import CapuletEngine, WilloughbyEngine, SternmanEngine


class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        engine = CapuletEngine(current_mileage=60000,
                               last_service_mileage=20000)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = CapuletEngine(current_mileage=30000,
                               last_service_mileage=20000)
        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        engine = WilloughbyEngine(
            current_mileage=70000, last_service_mileage=10000)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = WilloughbyEngine(
            current_mileage=40000, last_service_mileage=10000)
        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        engine = SternmanEngine(warning_light_is_on=True)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = SternmanEngine(warning_light_is_on=False)
        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main()
