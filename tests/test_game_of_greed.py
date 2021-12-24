import pytest
from game_of_greed.game_logic import GameLogic

# Testing - Roll Dice
# When rolling 1 to 6 dice ensure...
# A sequence of correct length is returned
# Each item in sequence is an integer with value between 1 and 6


def test_roll_six():
    roll = GameLogic.roll_dice(6)
    assert len(roll) == 6
    for value in roll:
        assert 1 <= value <= 6


def test_roll_five():
    roll = GameLogic.roll_dice(5)
    assert len(roll) == 5
    for value in roll:
        assert 1 <= value <= 6


# Hey! test_roll_six and test_roll_five are REALLY similar
# There's got to be a better way...


@pytest.mark.parametrize(
    "num_dice,expected_length",
    [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
    ],
)
def test_all_valid_dice_rolls(num_dice, expected_length):
    roll = GameLogic.roll_dice(num_dice)
    assert len(roll) == expected_length
    for value in roll:
        assert 1 <= value <= 6


# zilch - roll with no scoring dice should return 0
# ones - rolls with various number of 1s should return correct score
# twos - rolls with various number of 2s should return correct score
# threes - rolls with various number of 3s should return correct score
# fours - rolls with various number of 4s should return correct score
# fives - rolls with various number of 5s should return correct score
# sixes - rolls with various number of 6s should return correct score
# straight - 1,2,3,4,5,6 should return correct score
# three_pairs - 3 pairs should return correct score
# two_trios - 2 sets of 3 should return correct score
# leftover_ones - 1s not used in set of 3 (or greater) should return correct score
# leftover_fives - 5s not used in set of 3 (or greater) should return correct score
