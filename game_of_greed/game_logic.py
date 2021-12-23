import random


class GameLogic:
    @staticmethod
    def roll_dice(rolled_dice):
        dice_list = []
        for _ in range(rolled_dice):
            dice_list.append(random.randint(1, 6))
        return tuple(dice_list)

    @staticmethod
    def calculate_score(dice_roll):
        """
        Dice is a tuple of integers that represent a dice roll
        """
        score_table = {
            (1,): 100,
            (5,): 50,
            (1, 5): 150,
            (1, 1): 200,
            (5, 5): 100,
            (5, 1): 150,
            (1, 2, 3, 4, 5, 6): 1500,
            (6, 6, 6): 600,
            (6, 6, 6, 6): 1200,
            (6, 6, 6, 6, 6): 2400,
            (6, 6, 6, 6, 6, 6): 4800,
            (5, 5, 5): 500,
            (5, 5, 5, 5): 1000,
            (5, 5, 5, 5, 5): 2000,
            (5, 5, 5, 5, 5, 5): 4000,
            (4, 4, 4): 400,
            (4, 4, 4, 4): 800,
            (4, 4, 4, 4, 4): 1600,
            (4, 4, 4, 4, 4, 4): 3200,
            (3, 3, 3): 300,
            (3, 3, 3, 3): 600,
            (3, 3, 3, 3, 3): 1200,
            (3, 3, 3, 3, 3, 3): 2400,
            (2, 2, 2): 200,
            (2, 2, 2, 2): 400,
            (2, 2, 2, 2, 2): 800,
            (2, 2, 2, 2, 2, 2): 1600,
            (1, 1, 1): 1000,
            (1, 1, 1, 1): 2000,
            (1, 1, 1, 1, 1): 4000,
        }
        return score_table[dice_roll]
