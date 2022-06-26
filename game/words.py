import random
from game.terminal_service import TerminalService

class Word:
    """A list of words to use for the secret word. 
    """
    def __init__(self):
        self.terminal_service = TerminalService()
        self._list_of_words = ['country','product','delicious','outrageous','bag', 'eyes','encapsulation', 'classes','functions','programming','purpose']
        self.current_secret = self._get_secret_word()
        
    def draw(self, list_of_guesses):
        output = ""
        for letter in self.current_secret:
            if letter.lower() in list_of_guesses:
                output = output + letter + " "
            else:
                output = output + "_ "
        self.terminal_service.write_text(output)
    
    def get_current_secret(self):
        return self.current_secret

    def is_letter_in_secret(self, letter):
        return letter.lower() in self.current_secret.lower()

    def is_guessed(self, letters):
        result = True
        for letter in self.current_secret:
            if not letter.lower() in letters:
                result = False
        return result
   
    def too_many_guesses(self, letters):
        badGuesses = 0
        for guess in letters:
            if not guess in self.current_secret.lower():
                badGuesses += 1
        return badGuesses > 4

    def _get_secret_word(self):

        secret_word = random.choice(self._list_of_words).upper()
        return secret_word

        