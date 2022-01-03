class vehicle:

    def __init__(self, make, model, fuel="gas") -> None:
        self.make = make
        self.model = model
        self.fuel = fuel

    def is_eco_friendly(self) -> bool:
        if self.fuel == "gas":
            return False
        else:
            return True

class Car(vehicle):

    def __init__(self, make, model, fuel="gas", num_wheels=4) -> None:
        super().__init__(make, model, fuel=fuel)
        self.num_wheels = num_wheels
