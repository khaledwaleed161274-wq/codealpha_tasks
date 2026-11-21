# ============================================================
# CodeAlpha - Task 1: Hangman Game
# ============================================================

import random

WORDS = ["python", "codealpha", "intern", "logic", "script"]

MAX_WRONG = 6


def play_hangman():
    word = random.choice(WORDS)

    guessed_letters = []

    wrong_count = 0

    print("=== Hangman Game ===")
    print(f"The word has {len(word)} letters. You have {MAX_WRONG} wrong guesses.\n")

    while wrong_count < MAX_WRONG:

        display = []
        for letter in word:
            if letter in guessed_letters:
                display.append(letter)
            else:
                display.append("_")

        print("Word:", " ".join(display))

        if "_" not in display:
            print(f"\nCongratulations! You won! The word is: {word}")
            return

        print(f"Wrong guesses left: {MAX_WRONG - wrong_count}")
        print("Guessed letters:", ", ".join(sorted(guessed_letters)) or "None")

        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1:
            print("Error: please enter exactly one letter.\n")
            continue

        if not ("a" <= guess <= "z"):
            print("Error: please enter an English letter only.\n")
            continue

        if guess in guessed_letters:
            print("You already tried this letter! Try another one.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!\n")
        else:
            wrong_count += 1
            print("Wrong guess!\n")

    print(f"Game over. You lost! The word was: {word}")


if __name__ == "__main__":
    play_hangman()