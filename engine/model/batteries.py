from abc import ABC, abstractmethod
from datetime import datetime


class Battery(ABC):
    @abstractmethod
    def needs_service(self):
        pass


class NubbinBattery(Battery):
    def needs_service(self):
        # Implement the specific check for NubbinBattery
        pass


class SpindlerBattery(Battery):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        return (datetime.today() - self.last_service_date).days > (3 * 365)
