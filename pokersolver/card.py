import random
from enum import Enum

import itertools


class Suit(int, Enum):
    HEARTS = 1
    DIAMONDS = 2
    SPADES = 3
    CLUBS = 4


class Rank(int, Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


class Card:
    def __init__(self, rank, suit):
        self.suit = Suit(suit)
        self.rank = Rank(rank)

    def __str__(self):
        rank_str = str(self.rank.value) if self.rank < 11 else self.rank.name[0]
        suit_str = self.suit.name[0].lower()
        return f'{rank_str}{suit_str}'

    def __repr__(self):
        return str(self)


class Hand:
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

    def __str__(self):
        return f'{self.c1}{self.c2}'

    def __repr__(self):
        return str(self)


class Deck:
    def __init__(self, dead=None):
        self.cards = [Card(s, r) for s, r in itertools.product(Rank, Suit)]
        if dead:
            self.remove(*dead)
        random.shuffle(self.cards)

    def draw(self, amount):
        drawn = self.cards[:amount]
        self.cards = self.cards[:amount]
        return drawn

    def remove(self, *cards):
        for card in cards:
            self.cards.remove(card)
