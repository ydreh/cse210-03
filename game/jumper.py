from game.terminal_service import TerminalService
class Jumper:
    """Initiate the jumper """

    def __init__(self):

        self.terminal_service = TerminalService()
        self._guess = []
        self.bad_guess_count = 0
        self._parachute = [
            " _____ ",
            "/_____\ ",
            "\     / ",
            " \   /  ",
            "   O    ",
            " / | \  ",
            "  / \   ",
            "        ",
            "^^^^^^^"
            ]
    
    def made_bad_guess(self):
        if self.bad_guess_count >= 5:
            return
        self.bad_guess_count += 1
        self._parachute.pop(0)

    def draw(self):
        if self.bad_guess_count >= 5:
            self.terminal_service.write_text("   X    ")
        for i in self._parachute:
            self.terminal_service.write_text(i)