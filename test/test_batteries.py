import unittest
from datetime import datetime, timedelta
from engine.model.batteries import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_date = datetime.today() - timedelta(days=3*365)
        battery = SpindlerBattery(last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        last_service_date = datetime.today() - timedelta(days=2*365)
        battery = SpindlerBattery(last_service_date)
        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
