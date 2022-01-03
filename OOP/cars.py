# repl reload imported class
# import importlib
# importlib.reload(car)

class car:
    runs = True
    num_of_wheels = 4

    def __init__(self, name) -> None:
        self.name = name
        print(f"Does run {self.runs}")

    def __str__(self) -> str:
        return(f"{self.name} currently {self.runs}")

    def __repr__(self) -> str:
        return(f"car({self.name})")

    def start(self) -> None:
        if self.runs:
            print(f"{self.name} car is started")
        else:
            print(f"{self.name} car is broken :(")

    @classmethod
    def get_num_wheels(cls) -> int:
        return cls.num_of_wheels
