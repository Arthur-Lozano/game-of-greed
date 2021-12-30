from game_of_greed.game_logic import GameLogic


class Game:
    def play(self, roller=None):
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        user_response = input("> ")
        if user_response == "n":
            print("OK. Maybe another time")
        elif user_response == "y":
            die = GameLogic.roll_dice(6)
            print("Starting round 1\nRolling 6 dice...")
            # *** 4 4 5 2 3 1 ***
            die_string = " ".join([str(i) for i in die])
            print(f"*** {die_string} ***")
            balance = 0
            shelf = 0
            dice_remaing = 6
            play_q = input("Enter dice to keep, or (q)uit:\n> ")
            if play_q == "q":
                print(f"Thanks for playing. You earned {balance} points")
            else:
                score = GameLogic.calculate_score(tuple(int(i) for i in play_q))
                dice_remaing -= len(play_q)
                print(
                    f"You have {score} unbanked points and {dice_remaing} dice remaining"
                )


# E         +(r)oll again, (b)ank your points or (q)uit:
# E         +> b
# E         +You banked 50 points in round 1
# E         +Total score is 50 points
# E         +Starting round 2
# E         +Rolling 6 dice...
# E         +*** 6 4 5 2 3 1 ***
# E         +Enter dice to keep, or (q)uit:
# E         +> q
# E         +Thanks for playing. You earned 50 points
