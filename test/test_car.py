import unittest
from ..model.calliope import Calliope
from ..model.engines import CapuletEngine
from ..model.batteries import NubbinBattery


class TestCar(unittest.TestCase):
    def test_needs_service(self):
        # Example test case
        engine = CapuletEngine(current_mileage=50000,
                               last_service_mileage=20000)
        battery = NubbinBattery()
        car = Calliope(last_service_date, engine, battery)
        self.assertTrue(car.needs_service())


if __name__ == '__main__':
    unittest.main()
