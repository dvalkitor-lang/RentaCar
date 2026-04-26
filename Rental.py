from CarRent.Vehicle import Vehicle


class Rental:
    def __init__(self, name):
        self._name = name
        self._vehicles = []

    @property
    def name(self):
        return self._name

    @property
    def vehicles(self):
        for vehicle in self._vehicles:
            print(f"Gépjármű típusa: {vehicle.brand}, Rendszáma: {vehicle.license_plate}, Bérleti díj: {vehicle.rental_fee}, Kibérelve: {vehicle.is_booked}")

    @vehicles.setter
    def vehicles(self, new_rent):
        self._vehicles.append(new_rent)

    def book_by_license_plate(self, license_plate):
        for vehicle in self._vehicles:
            if vehicle.license_plate == license_plate:
                vehicle.book_vehicle()

    def unbook_by_license_plate(self, license_plate):
        for vehicle in self._vehicles:
            if vehicle.license_plate == license_plate:
                vehicle.unbook_vehicle()

