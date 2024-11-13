class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        self.is_running = True
        print(f"The {self.year} {self.brand} {self.model} has started.")

    def stop(self):
        self.is_running = False
        print(f"The {self.year} {self.brand} {self.model} has stopped.")

    def honk(self):
        print(f"The {self.brand} {self.model} honks: Beep beep!")

    def display_info(self):
        print(f"Vehicle Info: {self.year} {self.brand} {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors, fuel_type):
        super().__init__(brand, model, year)
        self.num_doors = num_doors
        self.fuel_type = fuel_type

    def start(self):
        super().start()
        print(f"The car runs on {self.fuel_type} fuel.")

    def honk(self):
        print(f"The {self.brand} {self.model} car honks: Honk Honk!")

    def display_info(self):
        super().display_info()
        print(f"Doors: {self.num_doors}, Fuel type: {self.fuel_type}")


class Truck(Vehicle):
    def __init__(self, brand, model, year, payload_capacity):
        super().__init__(brand, model, year)
        self.payload_capacity = payload_capacity

    def start(self):
        super().start()
        print(f"The truck is ready to carry a payload of {self.payload_capacity} tons.")

    def honk(self):
        print(f"The {self.brand} {self.model} truck honks: HONK HONK!")

    def display_info(self):
        super().display_info()
        print(f"Payload capacity: {self.payload_capacity} tons")


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_capacity):
        super().__init__(brand, model, year)
        self.engine_capacity = engine_capacity

    def start(self):
        super().start()
        print(f"The motorcycle with {self.engine_capacity}cc engine has started.")

    def honk(self):
        print(f"The {self.brand} {self.model} motorcycle honks: Beep beep!")

    def display_info(self):
        super().display_info()
        print(f"Engine capacity: {self.engine_capacity}cc")


def create_vehicle():
    print("\nSelect the type of vehicle you want to create:")
    print("1. Car")
    print("2. Truck")
    print("3. Motorcycle")
    
    choice = input("Enter your choice (1/2/3): ")

    brand = input("Enter vehicle brand: ")
    model = input("Enter vehicle model: ")
    year = input("Enter vehicle year: ")

    if choice == '1':
        num_doors = int(input("Enter number of doors: "))
        fuel_type = input("Enter fuel type (e.g., Gasoline, Diesel, Electric): ")
        return Car(brand, model, year, num_doors, fuel_type)
    
    elif choice == '2':
        payload_capacity = float(input("Enter payload capacity in tons: "))
        return Truck(brand, model, year, payload_capacity)
    
    elif choice == '3':
        engine_capacity = int(input("Enter engine capacity in cc: "))
        return Motorcycle(brand, model, year, engine_capacity)
    
    else:
        print("Invalid choice! Please select 1, 2, or 3.")
        return None


def main():
    while True:
        print("\n--- Vehicle Management System ---")
        print("1. Create a new vehicle")
        print("2. Display vehicle info")
        print("3. Start vehicle")
        print("4. Stop vehicle")
        print("5. Honk vehicle")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            vehicle = create_vehicle()
            if vehicle:
                print("\nVehicle created successfully!")
                vehicle.display_info()

        elif choice == '2' and 'vehicle' in locals():
            vehicle.display_info()

        elif choice == '3' and 'vehicle' in locals():
            vehicle.start()

        elif choice == '4' and 'vehicle' in locals():
            vehicle.stop()

        elif choice == '5' and 'vehicle' in locals():
            vehicle.honk()

        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("No vehicle created yet. Please create a vehicle first.")


if __name__ == "__main__":
    main()
