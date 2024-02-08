from abc import ABC, abstractmethod
from .service_criteria import MileageServiceCriteria, WarningLightServiceCriteria


class Engine(ABC):
    @abstractmethod
    def needs_service(self):
        pass


class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.mileage_criteria = MileageServiceCriteria(
            current_mileage, last_service_mileage)

    def needs_service(self):
        return self.mileage_criteria.should_be_serviced()


class WilloughbyEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.mileage_criteria = MileageServiceCriteria(
            current_mileage, last_service_mileage)

    def needs_service(self):
        return self.mileage_criteria.should_be_serviced()


class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on):
        self.warning_light_criteria = WarningLightServiceCriteria(
            warning_light_is_on)

    def needs_service(self):
        return self.warning_light_criteria.should_be_serviced()
