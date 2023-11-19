from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
    
    def needs_service(self):
        per_tire_wear_threshold = 0.9 
        tires_need_service = [
            x >= per_tire_wear_threshold 
            for x in self.tire_wear
        ]
        return any(tires_need_service)