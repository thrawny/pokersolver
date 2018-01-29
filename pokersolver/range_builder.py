import itertools

from pokersolver.card import Card, Hand, Rank
from pokersolver.utils import flatten

ALL_CARDS = Card.all()


def combos(r1, r2, suited=None):
    if r1 == r2:
        cards = [c for c in ALL_CARDS if c.rank == r1]
        return [Hand(c1, c2) for c1, c2 in itertools.combinations(cards, 2)]
    else:
        r1_cards = [c for c in ALL_CARDS if c.rank == r1]
        r2_cards = [c for c in ALL_CARDS if c.rank == r2]
        hands = [Hand(c1, c2) for c1, c2 in itertools.product(r1_cards, r2_cards)]
        if suited:
            return [h for h in hands if h.is_suited()]
        elif suited is False:
            return [h for h in hands if not h.is_suited()]
        else:
            return hands


# def gapper_builder(r1, r2, suited: bool = None):
#     """
#     86+ > 86, 97, T8, J9, QT, KJ, AQ
#     """
#     smaller, larger = sorted([r1, r2])
#     gap = larger - smaller
#     larger_ranks = list(Rank)[larger-gap::gap or None]
#     smaller_ranks = list(Rank)[smaller-gap::gap or None]
#     list_of_lists = (combos(x, y, suited) for x, y in zip(smaller_ranks, larger_ranks))
#     return flatten(list_of_lists)


def plus_builder_unpaired(r1, r2, suited: bool = None):
    """
    AT+ > AT, AJ, AQ, AK
    """
    if r1 == r2:
        raise ValueError('This function does not support pairs. Use plus_builder_paired.')
    smaller, larger = sorted([r1, r2])
    ascending_ranks = (r for r in Rank if smaller <= r < larger)
    list_of_lists = (combos(larger, x, suited) for x in ascending_ranks)
    return flatten(list_of_lists)


def plus_builder_paired(r):
    """
    JJ+ > JJ, QQ, KK, AA
    """
    ascending_ranks = (x for x in Rank if x >= r)
    list_of_lists = (combos(x, x) for x in ascending_ranks)
    return flatten(list_of_lists)


def plus_builder(r1, r2, suited: bool = None):
    if r1 == r2:
        return plus_builder_paired(r1)
    else:
        return plus_builder_unpaired(r1, r2, suited)


def _hand_range(sub_range: str):
    assert len(sub_range) in (2, 3, 4)
    r1, r2 = [Rank.from_str(r) for r in sub_range[:2]]

    suited = None
    if 's' in sub_range:
        suited = True
    elif 'o' in sub_range:
        suited = False

    if '+' in sub_range:
        return plus_builder(r1, r2, suited)
    else:
        return combos(r1, r2, suited)


def hand_range(range_str):
    hands = set()
    for sub_range in range_str.split(','):
        hands.update(set(_hand_range(sub_range)))
    return list(hands)
