from car import Car
from engine_folder.capulet_engine import CapuletEngine
from engine_folder.sternman_engine import SternmanEngine
from engine_folder.willoughby_engine import WilloughbyEngine  
from battery_folder.nubbin_battery import NubbinBattery
from battery_folder.spindler_battery import SpindlerBattery

class CarFactory():
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        return Car(engine,battery)
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        return Car(engine, battery)
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        return Car(engine,battery)

    @staticmethod
    def create_rorshach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        return Car(engine,battery)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        return Car(engine,battery)
