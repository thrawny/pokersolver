from typing import Optional

from pokersolver.card import Deck
from pokersolver.player import Player

CHECK = 0
BET = 1
RAISE = 2
NUM_ACTIONS = 3

NUM_PLAYERS = 2

MIN_BET = 2


def create_tree(flop, pot_size):
    deck = Deck(dead=flop)
    root = BoardCardNode(None)

    # p1 = Player()
    # p2 = Player()

    # Generate flop actions
    # for p in range(NUM_PLAYERS):
    #
    #     for a in range(NUM_ACTIONS):







class Node:
    def __init__(self, parent: Optional['Node']):
        self.parent = parent


class ActionNode(Node):
    def __init__(self, parent: 'Node', player):
        super(ActionNode, self).__init__(parent)
        self.player = player


class TerminalNode(Node):
    pass


class HoleCardNode(Node):
    pass


class BoardCardNode(Node):
    pass
