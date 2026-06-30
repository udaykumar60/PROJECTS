import random
MAX_TRIES = 6
words = [
    "programming", "computer", "keyboard", "hangman",
    "variable", "function", "algorithm", "compiler",
    "database", "network"
]
hints = [
    "Writing code",
    "Electronic device",
    "Input peripheral",
    "This game!",
    "Stores a value",
    "Reusable block",
    "Step-by-step procedure",
    "Translates code",
    "Stores data",
    "Connected computers"
]
STATE_MENU = 0
STATE_PLAYING = 1
STATE_WIN = 2
STATE_LOSE = 3
STATE_QUIT = 4
state = STATE_MENU
while state != STATE_QUIT:
    if state == STATE_MENU:
        print("\n=== WORD GUESS GAME ===")
        print("1. Play")
        print("2. Quit")
        choice = input("Choose: ")
        if choice == "1":
            n = random.randint(0, len(words) - 1)
            word = words[n]
            hint = hints[n]
            wrong = []
            state = STATE_PLAYING
        elif choice == "2":
            state = STATE_QUIT
        else:
            print("Please enter 1 or 2.")
    elif state == STATE_PLAYING:
        print(f"\nLives Remaining: {MAX_TRIES - len(wrong)}")
        print("Hint:", hint)
        if wrong:
            print("Wrong guesses:", ", ".join(wrong))
        guess = input("Enter the complete word: ").lower().strip()
        if not guess.isalpha():
            print(">> Please enter only alphabets.")
            continue
        if guess in wrong:
            print(">> You already guessed that word.")
            continue
        if guess == word:
            state = STATE_WIN
        else:
            wrong.append(guess)
            print(">> Wrong word!")
            if len(wrong) == MAX_TRIES:
                state = STATE_LOSE
    elif state == STATE_WIN:
        print("\n Congratulations! You guessed the word!")
        print("Word:", word)
        again = input("Play again? (y/n): ").lower()
        if again == "y":
            state = STATE_MENU
        else:
            state = STATE_QUIT
    elif state == STATE_LOSE:
        print("\n Game Over!")
        print("The correct word was:", word)
        again = input("Play again? (y/n): ").lower()
        if again == "y":
            state = STATE_MENU
        else:
            state = STATE_QUIT
print("\nGoodbye!")
