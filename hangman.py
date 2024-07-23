import random

def choose_word():
    words = [
    "hello", "world", "python", "program", "language",
    "computer", "science", "algorithm", "development", "engineer",
    "software", "application", "database", "network", "internet",
    "technology", "digital", "information", "system", "security",
    "communication", "business", "management", "organization", "project",
    "marketing", "strategy", "customer", "experience", "product",
    "service", "innovation", "global", "community", "education",
    "learning", "knowledge", "creative", "solution", "problem",
    "collaboration", "partnership", "teamwork", "fruit", "apple",
    "banana", "cherry", "orange", "grape"
] 
    return random.choice(words)

def display_word(word, guesses):
    displayed_word = ""
    for letter in word:
        if letter in guesses:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

def hangman():
    print("Welcome to Hangman!")
    print("Try to guess the word.")
    
    word = choose_word()
    guessed_letters = []
    incorrect_attempts = 0
    max_attempts = 6
    
    while incorrect_attempts < max_attempts:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print("right!")
        else:
            print("wrong!")
            incorrect_attempts += 1
        
        if all(letter in guessed_letters for letter in word):
            print("\n you guessed the word:", word)
            break
        
        print("Attempts remaining:", max_attempts - incorrect_attempts)
    
    if incorrect_attempts == max_attempts:
        print("\nSorry, you ran out of attempts. The word was:", word)

if __name__ == "__main__":
    hangman()
