from battery import Battery


class NubbinBattery(Battery):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)
    
    def needs_service(self):
        pass
