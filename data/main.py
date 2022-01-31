from .states.Tools import Control
from .states.Menu import Menu
from .states.Game import Game
from .states.Options import Options

def main():
    app = Control()
    state_dict = {"menu": Menu(),
                  "game": Game(),
                  "options": Options()
                  }
    app.setup_states(state_dict, "menu")
    app.main_game_loop()