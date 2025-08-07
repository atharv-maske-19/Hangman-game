import random


word_list = ['apple', 'banana', 'grape', 'orange', 'mango']


secret_word = random.choice(word_list)
guessed_letters = []
max_attempts = 6
attempts_left = max_attempts



display_word = ['_' for _ in secret_word]


print("Welcome to Hangman!")
print(f"The word has {len(secret_word)} letters.")



while attempts_left > 0 and '_' in display_word:
    print("\nCurrent word:", ' '.join(display_word))
    print(f"Attempts left: {attempts_left}")
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    
    guessed_letters.append(guess)

    
    if guess in secret_word:
        print("Good job! That letter is in the word.")
        for index, letter in enumerate(secret_word):
            if letter == guess:
                display_word[index] = guess
    else:
        print("Sorry, that letter is not in the word.")
        attempts_left -= 1



# Final outcome

if '_' not in display_word:
    print("\nCongratulations! You've guessed the word:", secret_word)
else:
    print("\nGame over. The word was:", secret_word)
