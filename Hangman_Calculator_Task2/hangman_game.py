import random 
 
def choose_word(): 
    words = ['python', 'hangman', 'challenge', 'programming', 'developer'] 
    return random.choice(words).upper() 
 
def play_game(): 
    word = choose_word() 
    guessed = ['_' for _ in word] 
    guessed_letters = set() 
    attempts = 6 
 
    print(" Welcome to Hangman!\n") 
 
    while attempts > 0 and '_' in guessed: 
        print('Word:', ' '.join(guessed)) 
        print(f'Attempts left: {attempts}') 
        print(f'Guessed letters: {" ".join(sorted(guessed_letters))}') 
        guess = input('Enter a letter: ').upper() 
 
        if not guess.isalpha() or len(guess) != 1: 
            print('Invalid input. Please enter a single letter.\n') 
            continue 
        if guess in guessed_letters: 
            print('You already guessed that letter.\n') 
            continue 
 
        guessed_letters.add(guess) 
        if guess in word: 
            for i, letter in enumerate(word): 
                if letter == guess: 
                    guessed[i] = guess 
        else: 
            attempts -= 1 
 
    if '_' not in guessed: 
        print(f'\n Congratulations! You guessed the word: {word}') 
    else: 
        print(f'\n Game Over. The word was: {word}') 
 
if __name__ == '__main__': 
    play_game()
