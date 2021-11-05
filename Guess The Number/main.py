logo = """
   /$$$$$$                                      /$$$$$$$$/$$                 /$$   /$$                         /$$                          
 /$$__  $$                                    |__  $$__/ $$                | $$$ | $$                        | $$                          
| $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$| $$  | $$$$$$$   /$$$$$$ | $$$$| $$ /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ 
| $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/| $$  | $$__  $$ /$$__  $$| $$ $$ $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$ | $$  | $$  \ $$| $$$$$$$$| $$  $$$$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$| $$  | $$  | $$| $$_____/| $$\  $$$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$      
|  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/| $$  | $$  | $$|  $$$$$$$| $$ \  $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$      
 \______/  \______/  \_______/|_______/|_______/ |__/  |__/  |__/ \_______/|__/  \__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/      



"""
import random
game_over = False


def generate_number():
    return random.randint(1, 101)


def compare(guess, number):
    if guess == number:
        global game_over
        game_over = True
        return f"You Win! {guess} was the number!"
    elif guess > number:
        if guess - number >= 10:
            return "Too high"
        else:
            return "A bit high"
    elif guess < number:
        if number - guess >= 10:
            return "Too low"
        else:
            return "A bit low"


def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = generate_number()
    number_of_guess = 0
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        number_of_guess = 10
    elif difficulty == "hard":
        number_of_guess = 5
    while number_of_guess > 0 and game_over == False:
        print(f"You have {number_of_guess} attempts remaining to guess the number.")
        guess = int(input("Guess a number: "))
        print(compare(guess, number))
        if game_over == True:
            break
        elif number_of_guess > 1:
            print("Guess again.")
        number_of_guess -= 1
    if game_over == False:
        print(f"You've run out of guesses, you lose. The number was {number}")


while input("Do you want to play Guess The Number game? Type 'y' or 'n': ") == "y":
    play_game()

print("Goodbye.")