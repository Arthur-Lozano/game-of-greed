# Lab: 06 - Game of Greed I - 12/23/2021

**Authors**: Wenhao Piao, Arthur Lozano

**Version**: 1.0.0

## Overview

Creating a Game of Greed game with Object Oriented Programming (OOP)

- `calculate_score` static method to GameLogic class.
  - The input to `calculate_score` is a tuple of integers that represent a dice roll.
  - The output from `calculate_score` is an integer representing the roll’s score according to rules of game.

- `roll_dice` method
  - The input to `roll_dice` is an integer between 1 and 6.
  - The output of `roll_dice` is a tuple with random values between 1 and 6.
  - The length of tuple must match the argument given to `roll_dice` method.

- Banker class
  - `shelf` instance method
    - Input to `shelf` is the amount of points (integer) to add to shelf.
    - `shelf` will temporarily store unbanked points.

  - `bank` instance method
    - `bank` adds any points on the shelf to total and reset shelf to 0.
    - `bank` output is the amount of points added to total from shelf.

  - `clear_shelf` instance method
    - `clear_shelf` removes all unbanked points.

## Getting started

1. Clone down the repo
2. CD into top-level directory of the repo
3. Run command `poetry install` to install the dependencies
4. See `game_logic.py`file to see the implementation of the classes
5. Run command `pytest` or `pytest --cov` to test the program
