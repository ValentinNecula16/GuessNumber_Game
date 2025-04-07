import random


EASY_LEVEL = 10
HARD_LEVEL = 5

def set_difficulty():
    difficulty = input('Choose difficulty: "easy" or "hard": ')
    if difficulty == "easy":
        return EASY_LEVEL
    elif difficulty == "hard":
        return HARD_LEVEL
    else:
        print("You need to choose 'easy' or 'hard'")
        return set_difficulty()


def check_answer(user_guess, actual_answer, turns):
    if user_guess < actual_answer:
        print("Too low")
        return turns - 1
    elif user_guess > actual_answer:
        print("Too high")
        return turns - 1
    else:
        print(f"Congrats! You guessed the number {actual_answer}")
        return turns


actual_answer = random.randint(1, 100)

def game():
    print("Welcome to Guess the Number!")
    turns = set_difficulty()

    guess = 0
    while guess != actual_answer:
        guess = int(input("Guess a number: "))
        turns = check_answer(guess , actual_answer ,turns)

        if turns == 0:
            print("You lost! The correct number was ", actual_answer)
            break
        else:
            print(f"You have {turns} attempts remaining.")
game()
