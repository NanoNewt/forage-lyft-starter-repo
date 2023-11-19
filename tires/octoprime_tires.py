from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
    def needs_service(self):
        total_tire_wear_threshould = 3
        return sum(self.tire_wear) >= total_tire_wear_threshould