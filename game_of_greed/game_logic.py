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
        grouped_dice = Counter(dice_roll)
        if len(grouped_dice) == 6:
            return 1500
        if len(grouped_dice) == 3:
            if [grouped_dice[num] for num in grouped_dice] == [2, 2, 2]:
                return 1500
        score = 0
        for num in grouped_dice:
            if grouped_dice[num] >= 3:
                if num != 1:
                    score += 100 * num * (grouped_dice[num] - 2)
                else:
                    score += 1000 * num * (grouped_dice[num] - 2)
            else:
                if num == 1:
                    score += 100 * grouped_dice[num]
                if num == 5:
                    score += 50 * grouped_dice[num]
        return score

    @staticmethod
    def get_scorers(dice):
        all_rolls_score = GameLogic.calculate_score(dice)
        if all_rolls_score == 0:
            return tuple()
        total = []
        for i in range(len(dice)):
            roll = dice[:i] + dice[i + 1 :]
            score = GameLogic.calculate_score(roll)
            if score != all_rolls_score:
                total.append(dice[i])
        return tuple(total)

    @staticmethod
    def validate_keepers(roll, keepers):
        list_possible_keepers = list(GameLogic.get_scorers(roll))
        list_possible_keepers.sort()
        list_keepers = list(keepers)
        list_keepers.sort()
        if list_keepers == list_possible_keepers:
            return True
        else:
            return False

    # another way to implement calculate_score method
    # @staticmethod
    # def calculate_score(dice_roll):
    #     """
    #     Dice is a tuple of integers that represent a dice roll
    #     """
    #     score_table = {
    #         (1, 1, 2, 2, 3, 3): 1500,
    #         (2, 2, 3, 3, 6, 6): 1500,
    #         (1, 2, 3, 4, 5, 6): 1500,
    #         (6, 6, 6): 600,
    #         (6, 6, 6, 6): 1200,
    #         (6, 6, 6, 6, 6): 1800,
    #         (6, 6, 6, 6, 6, 6): 2400,
    #         (5,): 50,
    #         (5, 5): 100,
    #         (5, 5, 5): 500,
    #         (5, 5, 5, 5): 1000,
    #         (5, 5, 5, 5, 5): 1500,
    #         (5, 5, 5, 5, 5, 5): 2000,
    #         (4, 4, 4): 400,
    #         (4, 4, 4, 4): 800,
    #         (4, 4, 4, 4, 4): 1200,
    #         (4, 4, 4, 4, 4, 4): 1600,
    #         (3, 3, 3): 300,
    #         (3, 3, 3, 3): 600,
    #         (3, 3, 3, 3, 3): 900,
    #         (3, 3, 3, 3, 3, 3): 1200,
    #         (2, 2, 2): 200,
    #         (2, 2, 2, 2): 400,
    #         (2, 2, 2, 2, 2): 600,
    #         (2, 2, 2, 2, 2, 2): 800,
    #         (1,): 100,
    #         (1, 1): 200,
    #         (1, 1, 1): 1000,
    #         (1, 1, 1, 1): 2000,
    #         (1, 1, 1, 1, 1): 3000,
    #         (1, 1, 1, 1, 1, 1): 4000,
    #     }

    #     sorted = list(dice_roll)
    #     sorted.sort()
    #     sorted_tuple = tuple(sorted)
    #     if sorted_tuple in score_table:
    #         return score_table[sorted_tuple]
    #     else:
    #         parsed_input = Counter(sorted_tuple)
    #         groups = []
    #         for i in parsed_input:
    #             group = []
    #             for j in range(parsed_input[i]):
    #                 group.append(i)
    #             groups.append(tuple(group))
    #         result = 0
    #         for group in groups:
    #             if group in score_table:
    #                 result += score_table[group]
    #         return result
