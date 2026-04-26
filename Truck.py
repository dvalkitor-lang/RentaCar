from Vehicle import Vehicle

class Truck(Vehicle):

    def __init__(self, license_plate, brand, rental_fee):
        super().__init__(license_plate, brand, rental_fee)
        self._extras=["Dízel üzem", "B kategóriával vezethető"]

    @property
    def license_plate(self):
        return self._license_plate

    @property
    def brand(self):
        return self._brand

    @property
    def rental_fee(self):
        return self._rental_fee

    @property
    def is_booked(self):
        return self._is_booked

    @property
    def extras(self):
        return self._extras

    def book_vehicle(self):
        if not self._is_booked:
            self._is_booked = True
        else:
            print("Az autó ki van bérelve jelenleg!")

    def unbook_vehicle(self):
        if self._is_booked:
            self._is_booked = False
            return True
        else:
            print("Az autó nincs kibérelve jelenleg!")
            return False