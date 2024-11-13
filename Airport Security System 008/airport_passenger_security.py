import random
import time

RESTRICTED_ITEMS = ['knife', 'gun', 'explosive', 'bomb', 'liquids over 100ml']

class Passenger:
    def __init__(self, name, passport_number, age, nationality):
        self.name = name
        self.passport_number = passport_number
        self.age = age
        self.nationality = nationality
        self.is_verified = False

    def verify_passport(self):
        if random.choice([True, False]):
            self.is_verified = True
            return True
        return False

class Baggage:
    def __init__(self, items):
        self.items = items

    def check_restricted_items(self):
        for item in self.items:
            if item in RESTRICTED_ITEMS:
                return False
        return True

class SecurityScreening:
    def __init__(self, passenger, baggage):
        self.passenger = passenger
        self.baggage = baggage
        self.passed = False

    def perform_screening(self):
        if not self.passenger.verify_passport():
            print(f"Passport check failed for {self.passenger.name}")
            return False
        if not self.baggage.check_restricted_items():
            print(f"Baggage check failed for {self.passenger.name}")
            return False
        self.passed = True
        return True

class Report:
    def __init__(self):
        self.passed_passengers = []
        self.failed_passengers = []

    def add_passed(self, passenger):
        self.passed_passengers.append(passenger)

    def add_failed(self, passenger):
        self.failed_passengers.append(passenger)

    def generate_report(self):
        print("\nSecurity Check Report")
        print("------------------------------------------------")
        print(f"Passengers who passed the security check: {len(self.passed_passengers)}")
        for p in self.passed_passengers:
            print(f"{p.name} - {p.passport_number}")
        print(f"Passengers who failed the security check: {len(self.failed_passengers)}")
        for p in self.failed_passengers:
            print(f"{p.name} - {p.passport_number}")
        print("------------------------------------------------")

def create_passenger():
    name = input("Enter passenger name: ")
    passport_number = input("Enter passport number: ")
    age = int(input("Enter passenger age: "))
    nationality = input("Enter nationality: ")
    return Passenger(name, passport_number, age, nationality)

def create_baggage():
    print("Enter items in the baggage (separate items by commas): ")
    items = input().split(',')
    items = [item.strip().lower() for item in items]
    return Baggage(items)

def main():
    report = Report()

    while True:
        print("\n--- Airport Security System ---")
        print("1. Add a new passenger")
        print("2. Generate security check report")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            passenger = create_passenger()
            baggage = create_baggage()
            screening = SecurityScreening(passenger, baggage)
            if screening.perform_screening():
                print(f"{passenger.name} passed the security check.")
                report.add_passed(passenger)
            else:
                print(f"{passenger.name} failed the security check.")
                report.add_failed(passenger)
            time.sleep(1)

        elif choice == '2':
            report.generate_report()

        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

