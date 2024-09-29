import random
EASY_LEVEL = 5
HARD_LEVEL = 2

answer = random.randint(1, 100)
def checkAnswer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")
        return turns - 1

def setDifficulty():
    """Asks the user to choose a difficulty level and returns the number of turns for that level."""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
      return EASY_LEVEL
    elif difficulty == 'hard':
      return HARD_LEVEL

def game():
    """Main game loop."""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    turns = setDifficulty()
    guess = 0
    while(guess != answer and turns != 0):
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = checkAnswer(guess, answer, turns)
      
    if turns == 0:
      print(f"You've run out of guesses, you lose. The answer was {answer}.")
      return
    else:
      print("Congratulations!!!")

game()