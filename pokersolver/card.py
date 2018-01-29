import itertools
import random
from enum import Enum


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

    @classmethod
    def from_str(cls, rank_str: str):
        if len(rank_str) != 1:
            raise ValueError('Only single characters can be converted to a rank.')
        rank_str = rank_str.upper()
        if rank_str.isnumeric():
            return cls(rank_str)
        elif rank_str == 'T':
            return cls.TEN
        elif rank_str == 'J':
            return cls.JACK
        elif rank_str == 'Q':
            return cls.QUEEN
        elif rank_str == 'K':
            return cls.KING
        elif rank_str == 'A':
            return cls.ACE
        raise ValueError(f'Unknown rank {rank_str}.')


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

    def __eq__(self, other: 'Card'):
        return self.rank == other.rank and self.suit == other.suit

    def __hash__(self):
        return hash((self.rank, self.suit))

    @staticmethod
    def all():
        return [Card(s, r) for s, r in itertools.product(Rank, Suit)]


class Hand:
    def __init__(self, c1: Card, c2: Card):
        if c1 == c2:
            raise ValueError('Cards in a hand must be unique.')
        self.c1 = c1
        self.c2 = c2

    def __str__(self):
        return f'{self.c1}{self.c2}'

    def __repr__(self):
        return str(self)

    def __iter__(self):
        for c in (self.c1, self.c2):
            yield c

    def __eq__(self, other: 'Hand'):
        return {self.c1, self.c2} == {other.c1, other.c2}

    def __hash__(self):
        return hash((self.c1, self.c2))

    def is_suited(self):
        return self.c1.suit == self.c2.suit

    @staticmethod
    def all():
        return [Hand(c1, c2) for c1, c2 in itertools.combinations(Card.all(), 2)]


class Deck:
    def __init__(self, dead=None):
        self.cards = Card.all()
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
