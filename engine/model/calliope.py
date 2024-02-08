from .car import Car
from .engines import CapuletEngine
from .batteries import NubbinBattery


class Calliope(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery()
        super().__init__(engine, battery)
