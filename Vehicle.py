from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, license_plate, brand, rental_fee):
        self._license_plate = license_plate
        self._brand = brand
        self._rental_fee = rental_fee
        self._is_booked = False
        self.extras = []


    def book_vehicle(self):
        pass

    def unbook_vehicle(self):
        pass





