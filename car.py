from abc import ABC, abstractmethod
from serviceable import Serviceable

class Car(ABC):
    def __init__(self,engine, battery, tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires

    @abstractmethod
    def needs_service(self):
        result = (
            self.engine.needs_service()
            or self.battery.needs_service()
            or self.tires.needs_service()
        )
        return result
