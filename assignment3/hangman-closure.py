# Task 4: Closure Practice


def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        display = "".join(c if c in guesses else "_" for c in secret_word)
        print(display)
        return all(c in guesses for c in secret_word)

    return hangman_closure


# Task 4: the hangman game
secret = input("Enter the secret word: ")
guess_letter = make_hangman(secret)
done = False
while not done:
    letter = input("Guess a letter: ")
    done = guess_letter(letter)
print("You got it!")
