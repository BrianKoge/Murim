# Base class: Warrior in Murim
class Warrior:
    def __init__(self, name, clan, level):
        self.name = name          # Name of the warrior
        self.clan = clan          # Clan they belong to
        self.level = level        # Martial arts level

    def attack(self):
        return f"{self.name} attacks with basic martial skills!"

    def meditate(self):
        return f"{self.name} meditates to restore energy."


# Subclass: Swordsman inherits from Warrior
class Swordsman(Warrior):
    def __init__(self, name, clan, level, sword_name):
        super().__init__(name, clan, level)  # Inherit base attributes
        self.sword_name = sword_name          # Unique attribute

    # Polymorphism: override attack method
    def attack(self):
        return f"{self.name} slashes fiercely with {self.sword_name}!"

    # New method specific to Swordsman
    def parry(self):
        return f"{self.name} parries the enemy's attack skillfully."


# Subclass: Archer inherits from Warrior
class Archer(Warrior):
    def __init__(self, name, clan, level, bow_name):
        super().__init__(name, clan, level)
        self.bow_name = bow_name

    def attack(self):
        return f"{self.name} shoots a precise arrow with {self.bow_name}!"


# Creating objects
warrior1 = Swordsman("Lee Jun", "Tiger Clan", 5, "Dragon Fang")
warrior2 = Archer("Han Soo", "Eagle Clan", 4, "Wind Whisper")

# Using methods
print(warrior1.attack())    # Lee Jun slashes fiercely with Dragon Fang!
print(warrior1.meditate())  # Lee Jun meditates to restore energy.
print(warrior1.parry())     # Lee Jun parries the enemy's attack skillfully.

print(warrior2.attack())    # Han Soo shoots a precise arrow with Wind Whisper!
print(warrior2.meditate())  # Han Soo meditates to restore energy.
