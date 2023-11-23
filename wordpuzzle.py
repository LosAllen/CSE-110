import random

def choose_secret_word():
    words = ["mosiah", "nephi", "helaman", "moroni", "alma", "abinadi"]
    return random.choice(words)

def display_hint(secret_word, guessed_word):
    hint = ""
    for sw, gw in zip(secret_word, guessed_word):
        if gw == sw:
            hint += gw.upper()
        elif gw in secret_word:
            hint += gw.lower()
        else:
            hint += "_"
    return hint

def main():
    print("Welcome to the word guessing game!")

    secret_word = choose_secret_word()
    guessed_word = ["_"] * len(secret_word)
    guesses = 0

    while True:
        print("Your hint is:", " ".join(guessed_word))
        guess = input("What is your guess? ").lower()

        if len(guess) != len(secret_word):
            print("Sorry, the guess must have the same number of letters as the secret word.")
        else:
            guesses += 1
            if guess == secret_word:
                print(f"Congratulations! You guessed it!\nIt took you {guesses} guesses.")
                break
            else:
                hint = display_hint(secret_word, guess)
                print("Your hint is:", " ".join(hint))
    
if __name__ == "__main__":
    main()