from game_of_greed.game_logic import GameLogic, Banker


class Game:
    def play(self, roller=GameLogic.roll_dice):
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        user_response = input("> ")
        if user_response == "n":
            print("OK. Maybe another time")
        elif user_response == "y":
            banker = Banker()
            round = 1
            total = 0
            # round start
            while True:
                die = roller(6)
                print(f"Starting round {round}\nRolling 6 dice...")
                die_string = " ".join([str(i) for i in die])
                print(f"*** {die_string} ***")
                dice_remaing = 6
                play_q = input("Enter dice to keep, or (q)uit:\n> ")
                if play_q == "q":
                    print(f"Thanks for playing. You earned {total} points")
                    break
                else:
                    score = GameLogic.calculate_score(tuple(int(i) for i in play_q))
                    banker.shelf(score)
                    dice_remaing -= len(play_q)
                    print(
                        f"You have {score} unbanked points and {dice_remaing} dice remaining"
                    )
                    roll_bank_quit = input(
                        "(r)oll again, (b)ank your points or (q)uit:\n> "
                    )
                    if roll_bank_quit == "b":
                        banker.bank()
                        total += score
                        print(f"You banked {banker.balance} points in round {round}")
                        print(f"Total score is {total} points")
                        round += 1
                        banker.balance = 0
                    elif roll_bank_quit == "q":
                        print(f"Thanks for playing. You earned {total} points")


# play the game
if __name__ == "__main__":
    game = Game()
    game.play()
