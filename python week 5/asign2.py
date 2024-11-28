class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving on the road. 🚗")

class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is flying through the air. ✈️")

class Boat(Vehicle):
    def move(self):
        print(f"{self.name} is sailing on the water. 🚢")

# Function to demonstrate polymorphism
def start_journey(vehicle):
    vehicle.move()

# Create instances of different vehicles
car = Car("Sports Car")
plane = Plane("Jumbo Jet")
boat = Boat("Cruise Ship")

# Demonstrate polymorphism
print("Starting journeys:")
start_journey(car)
start_journey(plane)
start_journey(boat)