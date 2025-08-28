# Base class: Ancient Animal in Murim
class AncientAnimal:
    def __init__(self, name):
        self.name = name

    def move(self):
        return f"{self.name} moves in a mysterious way."


# Subclass: Dragon inherits from AncientAnimal
class Dragon(AncientAnimal):
    def move(self):
        return f"{self.name} soars through the skies! 🐉"


# Subclass: Tiger inherits from AncientAnimal
class Tiger(AncientAnimal):
    def move(self):
        return f"{self.name} prowls silently through the forest! 🐅"


# Subclass: Turtle inherits from AncientAnimal
class Turtle(AncientAnimal):
    def move(self):
        return f"{self.name} slowly walks with ancient wisdom! 🐢"


# Subclass: Phoenix inherits from AncientAnimal
class Phoenix(AncientAnimal):
    def move(self):
        return f"{self.name} bursts into flames and flies gracefully! 🔥🕊️"


# Creating objects
dragon = Dragon("Azure Dragon")
tiger = Tiger("Shadow Tiger")
turtle = Turtle("Earth Turtle")
phoenix = Phoenix("Blazing Phoenix")

# List of all animals
ancient_animals = [dragon, tiger, turtle, phoenix]

# Demonstrating polymorphism
for animal in ancient_animals:
    print(animal.move())
