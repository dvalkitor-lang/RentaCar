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
            extras_text = ", ".join(vehicle.extras)
            print(f"Gépjármű típusa: {vehicle.brand},"
                  f" Rendszáma: {vehicle.license_plate}, "
                  f"Bérleti díj: {vehicle.rental_fee}, "
                  f"Extrák: {vehicle.extras}, "
                  f"Kibérelve: {vehicle.is_booked}")

    @vehicles.setter
    def vehicles(self, new_rent):
        self._vehicles.append(new_rent)

    def book_by_license_plate(self, license_plate):
        for vehicle in self._vehicles:
            if vehicle.license_plate == license_plate:
                return vehicle.book_vehicle()
        print("Nincs ilyen rendszámú jármű.")
        return False

    def unbook_by_license_plate(self, license_plate):
        for vehicle in self._vehicles:
            if vehicle.license_plate == license_plate:
                return vehicle.unbook_vehicle()
        print("Nincs ilyen rendszámú jármű.")
        return False
