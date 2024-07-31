import random

words = ["python", "ruby", "rust", "express", "flutter"]

chosen_word = random.choice(words)
length = len(chosen_word)
word_display = [
    "_" for _ in chosen_word
]  # this means _ will appear for every alphabet of the word

attempts = 4  # Number of allowed attempts


print("Welcome to Hangman!!")

print("The word is of length : ", length)

while attempts > 0 and "_" in word_display:
    print("\n" + " ".join(word_display))
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess  # revealing the letter
    else:
        print("That letter dosen't exist in the word")
        attempts -= 1


# game conclusion
if "_" not in word_display:
    print("you gussed the word correctly")
    print(" ".join(word_display))
    print("you survived")
else:
    print("You have lost all the attempts. The Word was", chosen_word)
    print("Game Over!!!")
