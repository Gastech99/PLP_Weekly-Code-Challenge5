# Classe parent
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def display_info(self):
        print(f"Hero: {self.name}, Power: {self.power}, City: {self.city}")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

# Classe enfant avec héritage
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.name} soars through the skies at {self.flight_speed} km/h!")


hero1 = Superhero("Shadow Knight", "Invisibility", "Gotham")
hero2 = FlyingHero("Sky Queen", "Wind Control", "Metropolis", 900)

hero1.display_info()
hero1.use_power()

hero2.display_info()
hero2.use_power()
