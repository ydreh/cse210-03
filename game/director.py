from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.words import Word

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    Attributes:
        _terminal_service: For getting and displaying information on the terminal.
        _jumper: is the player in the display that shows how many tries you have made
        is_playing (boolean): Whether or not to keep playing.
        _word_list:A list of word to be gueesed
        current_guesses[list]: is a list that stores the guesses
        recent_letter : the letter given by the user.
        
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._terminal_service = TerminalService()
        self._jumper = Jumper()
        self._is_playing = True
        self._word = Word()
        self.current_guesses = []
        self.recent_letter = ''

        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self._terminal_service.write_text("Welcome to Jumper game\n")
        self._do_outputs()
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
        self._terminal_service.write_text("See you next time!")


    def _do_outputs(self):

        self._word.draw(self.current_guesses)
        self._terminal_service.write_text("")
        self._jumper.draw()
        self._terminal_service.write_text("")
        if self._word.too_many_guesses(self.current_guesses):
            self._is_playing = False
        


    def _get_inputs(self):

        self.recent_letter = self._terminal_service.read_text("Guess a letter [a-z]: ")
        self.current_guesses.append(self.recent_letter.lower())

        
    def _do_updates(self):
 
        if self._word.is_letter_in_secret(self.recent_letter) == False:
            self._jumper.made_bad_guess()

        if self._word.is_guessed(self.current_guesses):
            self._is_playing = False
        
    def _do_updates(self):
 
        if self._word.is_letter_in_secret(self.recent_letter) == False:
            self._jumper.made_bad_guess()

        if self._word.is_guessed(self.current_guesses):
            self._is_playing = False
    
   