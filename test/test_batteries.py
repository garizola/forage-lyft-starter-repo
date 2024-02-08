import unittest
# Include other batteries as needed
from engine.model.batteries import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        battery = NubbinBattery(last_service_date=datetime(
            2020, 1, 1), current_date=datetime(2024, 1, 1))
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        battery = NubbinBattery(last_service_date=datetime(
            2023, 1, 1), current_date=datetime(2024, 1, 1))
        self.assertFalse(battery.needs_service())

# Other battery tests would follow a similar structure


if __name__ == '__main__':
    unittest.main()
