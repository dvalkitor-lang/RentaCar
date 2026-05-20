from Rental import Rental
from Car import Car
from Truck import Truck

class Booking:
    def __init__(self):
        self._rental=Rental("Kovács és Tesó kölcsönző")
        self._init_data()

    def _init_data(self):
        self._rental.vehicles = Car("TES-001", "Trabant", 1000)
        self._rental.vehicles = Car("TES-002", "Lada", 2000)
        self._rental.vehicles = Car("TES-003", "Porsche", 5000)
        self._rental.vehicles = Truck("KOV-001", "Man", 2000)
        self._rental.vehicles = Truck("KOV-002", "Volvo", 2500)
        self._rental.vehicles = Truck("KOV-003", "Scania", 2200)
        self._rental.vehicles = Truck("KOV-004", "Iveco", 4000)

    def user_interaction(self):
            while True:
                print("\n" + "=" * 35)
                print(f"   {self._rental.name.upper()}")
                print("=" * 35)
                print("1. Gépjárművek listázása")
                print("2. Gépjármű bérlése")
                print("3. Bérlés lemondása")
                print("4. Kilépés")

                while True:
                    try:
                        menu = int(input("Válassz a fenti menüpontokból: "))
                        break
                    except ValueError:
                        print("1-4 között add meg a kívánt menüpont számát!")
                if menu == 1:
                    self._rental.vehicles
                elif menu == 2:
                    license_plate = input("Add meg a rendszámot: ").upper()
                    success = self._rental.book_by_license_plate(license_plate)
                    if success:
                        for v in self._rental._vehicles:
                            if v.license_plate == license_plate:
                                print(f"Bérlés sikeres. Napi díj: {v.rental_fee} Ft")
                elif menu == 3:
                    license_plate = input("Add meg a rendszámot!").upper()
                    success = self._rental.unbook_by_license_plate(license_plate)
                    if success:
                        print("Bérlés lemondva.")

                elif menu == 4:
                    print("\n Kilépés... Viszontlátásra!")
                    break

booking = Booking()
booking.user_interaction()
