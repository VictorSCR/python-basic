from homework_02.exceptions import LowFuelError, NotEnoughFuel

from abc import ABC

class Vehicle(ABC):
    started = False

    def __init__(self, weight = 1700, fuel = 60, fuel_consumption = 10):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance):
        rep = distance * self.fuel_consumption
        if rep <= self.fuel:
            self.fuel -= rep
        else:
            raise NotEnoughFuel

