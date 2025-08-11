class Car:
    def move(self):
        print("Driving")

class Plane:
    def move(self):
        print("Flying")

class Boat:
    def move(self):
        print("Sailing")

vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
