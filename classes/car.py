class Car:
    make ="Chevrolet"

    def __init__(self, make, model, fuel_efficiency):
        self.make = make
        self.model = model
        self.fuel_efficiency = fuel_efficiency
    def check_model(self):
        return f"I am suprised that Camaro is a car brand for {self.make}"
