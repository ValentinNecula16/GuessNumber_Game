# Guess the Number Game

A simple number guessing game implemented in Python.

## How to Play

- The game will randomly generate a number between 1 and 100.
- You will need to guess the number within a limited number of attempts based on the difficulty you choose.
- There are two difficulty levels:
  - **Easy**: 10 attempts
  - **Hard**: 5 attempts
- After each guess, the game will tell you if your guess is too high or too low.
- If you guess correctly, you win. If you run out of attempts, you lose.

## How to Run

1. Clone the repository to your local machine.
2. Make sure you have Python installed.
3. Run the script:
   ```bash
   python guess_the_number.py

Example of the Game Flow:
Welcome to Guess the Number!
Choose difficulty: "easy" or "hard": easy
Guess a number: 50
Too low
You have 9 attempts remaining.
Guess a number: 75
Too high
You have 8 attempts remaining.
Guess a number: 60
Congrats! You guessed the number 60
