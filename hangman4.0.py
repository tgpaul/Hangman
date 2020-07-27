from words import w_list
#words.py is a file containing a list of words.
import random

#Function to get a random word from the file "words.py".
def get_word():
    word = random.choice(w_list)
    return word.upper()

#Function to display the design of the hangman for each stage or try.
def display_hangman(life):
    stages = [
    """
      -------
      |     |
      |     O
      |    /|\\
      |     |
      |    / \\
     ---
    """,
    """
      -------
      |     |
      |     O
      |    /|
      |     |
      |    / \\
     ---
    """,
    """
      -------
      |     |
      |     O
      |     |
      |     |
      |    / \\
     ---
    """,
    """
      -------
      |     |
      |     O
      |     |
      |     |
      |      \\
     ---
    """,
    """
      -------
      |     |
      |     O
      |     |
      |     |
      |
     ---
    """,
    """
      -------
      |     |
      |     O
      |     |
      |
      |
     ---
    """,
    """
      -------
      |     |
      |     O
      |
      |
      |
     ---
    """,
    """
      -------
      |     |
      |
      |
      |
      |
     ---
    """,
    """
      -------
      |
      |
      |
      |
      |
     ---
    """,
    ]
    return stages[life]

#Function with the actuall game. Records players guesses and state.
def play(word):
    #Initiate all variables. Start of game.
    #Variable to keep word progress.
    word_completion = "*" * len(word)
    #Variable to keep game progress
    guessed = False
    #variable to store guessed letters.
    g_letters = []
    #Variable to keep guessed words.
    g_words = []
    #variables for number of tries
    life = 8

    print("\t\t\tLets play hangman!!......\n\t\t\tGuess the district in Kerala")
    print(display_hangman(life))
    print(word_completion)
    print("\n")

    while not guessed and life > 0:
        guess = input("\t\t\tGuess a word or a letter : ").upper()

        #Consider that the user entered a letter.
        if len(guess) == 1 and guess.isalpha():
            if guess in g_letters:
                print("\t\t\tYou have already guessed ",guess)
            elif guess not in word:
                print("\t\t\t"+guess+" IS NOT in the word")
                life -= 1
                g_letters.append(guess)
            else:
                print("\t\t\t"+guess+" IS present in the word")

                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess

                word_completion = "".join(word_as_list)
                if "*" not in word_completion:
                    guessed = True

        #Consider that the user entered a word.
        elif len(guess) == len(word) and guess.isalpha():
            if guess in g_words:
                print("\t\t\t"+guess+" has already been guessed.")
            elif guess != word:
                print("\t\t\t"+guess+" IS NOT the word")
                life -= 1
                g_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("\t\t\tInvalid Guess!\n")

        print(display_hangman(life))
        print(word_completion)
        print("\n")

    if guessed:
        print("\t\t\tCongratulations! You won!")
    else:
        print("\t\t\tYou have run out of tries.\nThe word was "+word+"\nBetter luck next time.")

if __name__ == "__main__":
    word = get_word()
    play(word)
    while input("\t\t\tDo you want to play again (Y/N) : ").upper() == "Y":
        word = get_word()
        play(word)
