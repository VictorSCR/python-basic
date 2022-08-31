from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 100

    def __init__(self, weight = 1700, fuel = 60, fuel_consumption = 10, max_cargo = 100):
        super(Plane, self).__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo


    def load_cargo(self, cargo):
        gruz = self.cargo + cargo
        if gruz > self.max_cargo:
            raise CargoOverload
        self.cargo = gruz

    def remove_all_cargo(self):
        a = self.cargo
        self.cargo = 0
        return a

