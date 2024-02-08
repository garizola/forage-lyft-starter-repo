from abc import ABC, abstractmethod


class Battery(ABC):
    @abstractmethod
    def needs_service(self):
        pass


class NubbinBattery(Battery):
    def needs_service(self):
        # Implement the specific check for NubbinBattery
        pass
