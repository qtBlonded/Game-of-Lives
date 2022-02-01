from .components.Tools import Control
from .states.Menu import Menu
from .states.Game import Game
from .states.Options import Options
from .states.How_to_play import How_to_play


def main():
    app = Control()
    state_dict = {"menu": Menu(),
                  "game": Game(),
                  "options": Options(),
                  "how_to_play": How_to_play()
                  }
    app.setup_states(state_dict, "menu")
    app.main_game_loop()