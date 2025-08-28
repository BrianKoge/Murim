# Murim OOP Adventure 🐉⚔️

## Description
This project uses a Murim-themed world of ancient animals and warriors to demonstrate core OOP principles in Python: **inheritance, polymorphism, and encapsulation**.

## Features
- **Ancient Animals**: Dragon, Tiger, Turtle, Phoenix with unique `move()` methods (polymorphism).  
- **Warriors**: Swordsman and Archer inheriting from Warrior with custom `attack()` methods.  
- Demonstrates constructors, method overriding, and class inheritance.

## Example

```python
dragon = Dragon("Azure Dragon")
print(dragon.move())  # Azure Dragon soars through the skies! 🐉

warrior1 = Swordsman("Lee Jun", "Tiger Clan", 5, "Dragon Fang")
print(warrior1.attack())   # Lee Jun slashes fiercely with Dragon Fang!
