from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
import sys


class Game:
    def __init__(self, num_rounds=None):
        self.num_rounds = num_rounds
        self.round = 1
        self.dice_remaining = 6
        self.banker = Banker()

    def play(self, roller=None):
        if roller == None:
            roller = GameLogic.roll_dice
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        user_response = input("> ")
        if user_response == "n":
            print("OK. Maybe another time")
        elif user_response == "y":
            self.start_round(roller)

    def start_round(self, roller):
        self.dice_remaining = 6
        print(f"Starting round {self.round}\nRolling {self.dice_remaining} dice...")
        dice = self.roll_die(roller, self.dice_remaining)
        self.keep_or_q(roller, dice)

    def convert_to_dice_string(self, dice):
        dice_string = " ".join([str(i) for i in dice])
        print(f"*** {dice_string} ***")

    def roll_die(self, roller, roll):
        dice = roller(roll)
        self.convert_to_dice_string(dice)
        return dice

    def roll_again(self, roller, remaining_dice):
        print(f"Rolling {remaining_dice} dice...")
        dice = self.roll_die(roller, remaining_dice)
        if GameLogic.calculate_score(dice) == 0:
            print(
                "****************************************\n**        Zilch!!! Round over         **\n****************************************"
            )
            print(f"You banked 0 points in round {self.round}")
            print(f"Total score is {self.banker.balance} points")
            self.round += 1
            self.start_round(roller)
        else:
            self.keep_or_q(roller, dice)

    def roll_bank_quit(self, roller):
        print("(r)oll again, (b)ank your points or (q)uit:")
        r_b_q = input("> ")
        if self.dice_remaining == 0:
            self.dice_remaining = 6
        if r_b_q == "q":
            self.quit()
        elif r_b_q == "r":
            self.roll_again(roller, self.dice_remaining)
        elif r_b_q == "b":
            this_round_points = self.banker.shelved
            self.banker.bank()
            print(f"You banked {this_round_points} points in round {self.round}")
            print(f"Total score is {self.banker.balance} points")
            if self.num_rounds:
                self.num_rounds -= 1
                if self.num_rounds == 0:
                    self.quit()
            else:
                self.round += 1
                self.start_round(roller)

    def validate_input(self, dice):
        while True:
            print("Enter dice to keep, or (q)uit:")
            play_q = input("> ")
            play_q = play_q.replace(" ", "").strip()
            if play_q == "q":
                self.quit()
                break
            else:
                tuple_play_q = tuple(int(i) for i in play_q)
                if GameLogic.validate_keepers(dice, tuple_play_q):
                    return tuple_play_q
                else:
                    print(f"Cheater!!! Or possibly made a typo...")
                    self.convert_to_dice_string(dice)

    def keep_or_q(self, roller, dice):
        validated_dice = self.validate_input(dice)
        score = GameLogic.calculate_score(validated_dice)
        self.banker.shelf(score)
        self.dice_remaining -= len(validated_dice)
        print(
            f"You have {self.banker.shelved} unbanked points and {self.dice_remaining} dice remaining"
        )
        self.roll_bank_quit(roller)

    def quit(self):
        print(f"Thanks for playing. You earned {self.banker.balance} points")
        self.banker.balance = 0
        self.banker.clear_shelf()
        sys.exit()


# play the game
if __name__ == "__main__":
    game = Game()
    game.play()
