class Vehicle:

    def __init__(self, make, model, fuel="gas") -> None:
        self.make = make
        self.model = model
        self.fuel = fuel

    def __str__(self):
        return(f"I drive a {self.make} {self.model} and it runs on {self.fuel}.")

class Car(Vehicle):
    num_wheels = 4

class Truck(Vehicle):
    num_wheels = 6

    def __init__(self, make, model, fuel="diesel") -> None:
        super().__init__(make, model, fuel=fuel)

# daily = Vehicle("Lamborghini", "Aventador")
# print(daily)

class GitHubRepo:
    def __init__(self, name, language, stars) -> None:
        self.name = name
        self.language = language
        self.stars = stars

    def __str__(self) -> str:
        return(f"-> {self.name} is a {self.language} repo with {self.stars} stars")

vue = GitHubRepo("Vue", "JavaScript", 50000)
print(vue)
