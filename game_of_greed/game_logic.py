import random

class GameLogic:

    @staticmethod
    def roll_dice(rolled_dice):
        dice_list = []
        for _ in range(rolled_dice):
            dice_list.append(random.randint(1,6))
        return tuple(dice_list)

    @staticmethod
    def calculate_score(calculate_score)
    """
    Dice is a tuple of integers that represent a dice roll
    """
        