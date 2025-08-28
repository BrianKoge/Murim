# Murim OOP Adventure 🐉⚔️

## Description
This project demonstrates **Object-Oriented Programming (OOP) concepts** in Python using a **Murim-themed world**.  
It includes:  

- **Ancient Animals**: Dragon, Tiger, Turtle, Phoenix  
- **Warriors**: Swordsman and Archer  
- **OOP Principles**:  
  - **Inheritance**: Subclasses inherit from base classes.  
  - **Polymorphism**: Methods like `move()` and `attack()` behave differently for each subclass.  
  - **Encapsulation**: Attributes are initialized via constructors.  

---

## Features

### 1. Ancient Animals
- Each animal has a `move()` method that behaves differently.  
- Demonstrates **polymorphism** in action.  

### Example:

```python
dragon = Dragon("Azure Dragon")
print(dragon.move())  # Azure Dragon soars through the skies! 🐉

### 2. Warriors

- Swordsman and Archer inherit from Warrior.

- Each class overrides the attack() method differently.

- Additional methods like parry() and meditate() simulate Murim combat.

### Example:

```python
warrior1 = Swordsman("Lee Jun", "Tiger Clan", 5, "Dragon Fang")
print(warrior1.attack())   # Lee Jun slashes fiercely with Dragon Fang!
print(warrior1.meditate()) # Lee Jun meditates to restore energy.

## How to Run
- Make sure Python 3.x is installed.
- Copy the codes into a Python file
- Run the file
