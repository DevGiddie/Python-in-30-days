import random

class RetroRunGame:
    def __init__(self):
        self.player_position = 0
        self.finish_line = 50

    def play(self):
        print("Welcome to Retro Run!")
        print("Get ready for a nostalgic racing experience!")

        while self.player_position < self.finish_line:
            self.show_player_position()
            self.show_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.race()
            else:
                print("Invalid choice. Try again.")

    def show_player_position(self):
        print(f"You are currently at position {self.player_position}.")

    def show_menu(self):
        print("----- Menu -----")
        print("1. Accelerate")
        print("-----------------")

    def race(self):
        acceleration = random.randint(1, 10)
        self.player_position += acceleration
        print(f"You accelerated by {acceleration} units!")

    def check_finish_line(self):
        if self.player_position >= self.finish_line:
            print("Congratulations! You reached the finish line!")

# Start the game
game = RetroRunGame()
game.play()
