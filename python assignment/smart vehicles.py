class Vehicle:
    def move(self):
        print("This vehicle moves somehow.")


class StarletCar(Vehicle):
    def move(self):
        print("Starlet Car is driving smoothly 🚗")


class StarletPlane(Vehicle):
    def move(self):
        print("Starlet Plane is flying with AI autopilot ✈️")


class StarletBoat(Vehicle):
    def move(self):
        print("Starlet Boat is sailing with green energy 🚤")


# Example usage
vehicles = [StarletCar(), StarletPlane(), StarletBoat()]

for v in vehicles:
    v.move()
