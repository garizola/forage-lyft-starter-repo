from datetime import datetime
from abc import ABC, abstractmethod


class ServiceCriteria(ABC):
    @abstractmethod
    def should_be_serviced(self):
        pass


class MileageServiceCriteria(ServiceCriteria):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 30000


class DateServiceCriteria(ServiceCriteria):
    def __init__(self, last_service_date, years):
        self.last_service_date = last_service_date
        self.years = years

    def should_be_serviced(self):
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + self.years)
        return service_threshold_date < datetime.today().date()


class WarningLightServiceCriteria(ServiceCriteria):
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def should_be_serviced(self):
        return self.warning_light_is_on
