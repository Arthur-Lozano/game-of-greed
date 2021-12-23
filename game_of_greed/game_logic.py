import random
from collections import Counter


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
            (1, 2, 3, 4, 5, 6): 1500,
            (6, 6, 6): 600,
            (6, 6, 6, 6): 1200,
            (6, 6, 6, 6, 6): 1800,
            (6, 6, 6, 6, 6, 6): 2400,
            (5,): 50,
            (5, 5): 100,
            (5, 5, 5): 500,
            (5, 5, 5, 5): 1000,
            (5, 5, 5, 5, 5): 1500,
            (5, 5, 5, 5, 5, 5): 2000,
            (4, 4, 4): 400,
            (4, 4, 4, 4): 800,
            (4, 4, 4, 4, 4): 1200,
            (4, 4, 4, 4, 4, 4): 1600,
            (3, 3, 3): 300,
            (3, 3, 3, 3): 600,
            (3, 3, 3, 3, 3): 900,
            (3, 3, 3, 3, 3, 3): 1200,
            (2, 2, 2): 200,
            (2, 2, 2, 2): 400,
            (2, 2, 2, 2, 2): 600,
            (2, 2, 2, 2, 2, 2): 800,
            (1,): 100,
            (1, 1): 200,
            (1, 1, 1): 1000,
            (1, 1, 1, 1): 2000,
            (1, 1, 1, 1, 1): 3000,
            (1, 1, 1, 1, 1, 1): 4000,
        }

        # sorted = tuple(list(dice_roll).sort())
        sorted = list(dice_roll)
        sorted.sort()
        sorted_tuple = tuple(sorted)
        if sorted_tuple in score_table:
            return score_table[sorted_tuple]
        else:
            parsed_input = Counter(dice_roll)
            # to do: group the same numbers in the tuple
            groups = []
            for i in parsed_input:
                group = []
                for j in range(parsed_input[i]):
                    group.append(i)
                    # [3, 3, 3]
                groups.append(tuple(group))
            result = 0
            for group in groups:
                if group in score_table:
                    result += score_table[group]
                # else:
                #     result += 0
            print(result)
            return result


# Testing
input = (3, 3, 3, 2, 2, 2, 2, 1)
GameLogic.calculate_score(input)
