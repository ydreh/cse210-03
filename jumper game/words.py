import random

words = ['country','product','delicious','outrageous','bag']

class Word:
    
    def __init__(self):
        self.word = random.choice(words)
        self.display = ["_" for letter in self.word]
        self.guesses = 0

    def show(self):
        display =  "  ".join(self.display)
        print(f"the word is: {display}")

    def get_word_index(self, guess):
        locations = []

        for index, char in enumerate(list(self.word)):
            if char == guess:
                locations.append(index)

        return locations
    
    def update(self, index, letter):
        for number in index:
            self.display[index] = letter

    def check_guess(self, guess):
        if guess in self.word:
            index = self.get_word_indes(guess)
            self.update(index, guess)
    
    def check_for_win(self):
        display = ''.join(self.display)
        word = self.word
        if display == word:
            print("You Win!!!")
            return True