
# Base class
class Character:
    def __init__(self, name, age, origin):
        self.name = name
        self.age = age
        self.origin = origin
        self.__secret_identity = "Unknown"  # Encapsulated attribute

    def introduce(self):
        return f"My name is {self.name}, I am from {self.origin}."

    def set_secret_identity(self, identity):
        self.__secret_identity = identity

    def get_secret_identity(self):
        return self.__secret_identity

# Derived class
class Superhero(Character):
    def __init__(self, name, age, origin, power, team):
        super().__init__(name, age, origin)
        self.power = power
        self.team = team

    def use_power(self):
        return f"{self.name} uses {self.power}!"

    def introduce(self):
        base_intro = super().introduce()
        return f"{base_intro} I fight for justice with the {self.team}!"

# Test
hero1 = Superhero("ShadowStrike", 28, "Night City", "Invisibility", "Night Watchers")
hero1.set_secret_identity("Lena Vale")

print(hero1.introduce())
print(hero1.use_power())
print("Secret Identity:", hero1.get_secret_identity())

