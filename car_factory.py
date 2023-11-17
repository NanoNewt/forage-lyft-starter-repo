from car import Car
from engine_folder.engine import Engine
from battery_folder.battery import Battery

class CarFactory():
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(last_service_date, Engine(last_service_date), Battery(last_service_date))
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(last_service_date, Engine(last_service_date), Battery(last_service_date))
    def create_palindrome(current_date, last_service_date, current_mileage, warning_light_on):
        return Car(last_service_date, Engine(last_service_date,warning_light_on), Battery(last_service_date))
    def create_rorshach(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(last_service_date, Engine(last_service_date), Battery(last_service_date))
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(last_service_date, Engine(last_service_date), Battery(last_service_date))