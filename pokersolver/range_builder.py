import itertools

from pokersolver.card import Suit, Rank, Card, Hand, Deck


d = set(Deck().cards)


def combos(r1, r2):
    cards = [c for c in d if c.rank in (r1, r2)]
    return [Hand(c1, c2) for c1, c2 in itertools.combinations(cards, 2)]


def plus_builder(r1, r2, suited=None):
    hands = []

    smaller, larger = sorted([r1, r2])
    gap = larger - smaller













# def _hand_range(sub_range: str):
#     if len(sub_range) == 3:
#         # AQo or AQs
#         combo = sub_range[:2]
#         builder = sub_range[2]
#         if builder == '+':
#
#     elif len(sub_range) == 4:
#         # specific hand, 9h9c
#     elif len(sub_range) == 2:
#         # specific ranks, 99, AQ etc.


# def hand_range(range_str):
#     for sub_range in range_str.split(','):
#         pass
