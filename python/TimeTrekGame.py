import random

class TimeTrekGame:
    def __init__(self):
        self.player_position = 0
        self.finish_line = 100

    def play(self):
        print("Welcome to Time Trek!")
        print("Race through different historical eras to reach the finish line!")
        print("You are currently in the present time.")

        while self.player_position < self.finish_line:
            self.show_player_position()
            self.show_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.race()
            elif choice == "2":
                self.travel()
            else:
                print("Invalid choice. Try again.")

    def show_player_position(self):
        print(f"You are currently at position {self.player_position}.")

    def show_menu(self):
        print("----- Menu -----")
        print("1. Race")
        print("2. Travel to a different time")
        print("-----------------")

    def race(self):
        distance = random.randint(1, 10)
        self.player_position += distance
        print(f"You raced ahead by {distance} units!")

    def travel(self):
        print("Select a time to travel:")
        print("1. Ancient Times")
        print("2. Medieval Era")
        print("3. Future World")
        choice = input("Enter your choice: ")

        if choice == "1":
            self.player_position += 20
            print("You traveled to Ancient Times and advanced 20 units!")
        elif choice == "2":
            self.player_position += 15
            print("You traveled to the Medieval Era and advanced 15 units!")
        elif choice == "3":
            self.player_position += 25
            print("You traveled to the Future World and advanced 25 units!")
        else:
            print("Invalid choice. Try again.")

        if self.player_position >= self.finish_line:
            print("Congratulations! You reached the finish line!")

# Start the game
game = TimeTrekGame()
game.play()
