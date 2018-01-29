from pokersolver import range_builder
from pokersolver.card import Card, Hand, Rank


def test_combos_unpaired():
    combos = range_builder.combos(8, 6)
    pair = Hand(Card(6, 1), Card(6, 2))
    eight_six = Hand(Card(8, 1), Card(6, 2))
    assert pair not in combos
    assert eight_six in combos
    assert len(combos) == 16


def test_combos_paired():
    combos = range_builder.combos(6, 6)
    pair = Hand(Card(6, 1), Card(6, 2))
    eight_six = Hand(Card(8, 1), Card(6, 2))
    assert pair in combos
    assert eight_six not in combos
    assert len(combos) == 6


def test_combos_suited():
    combos = range_builder.combos(8, 6, suited=True)
    eight_six_off = Hand(Card(8, 1), Card(6, 2))
    eight_six_suited = Hand(Card(8, 1), Card(6, 1))
    assert eight_six_suited in combos
    assert eight_six_off not in combos
    assert len(combos) == 4


# def test_gapper_builder_unpaired():
#     combos = range_builder.gapper_builder(8, 6)
#     assert len(combos) == 16 * 4
#
#
# def test_gapper_builder_paired():
#     combos = range_builder.gapper_builder(6, 6)
#     assert len(combos) == 6 * 7


def test_plus_builder():
    combos = range_builder.plus_builder_unpaired(14, 11)
    assert len(combos) == 16 * 3
    assert combos == range_builder.combos(14, 11) + range_builder.combos(14, 12) + range_builder.combos(14, 13)


def test_plus_builder_paired():
    combos = range_builder.plus_builder_paired(6)
    print(combos)
    assert len(combos) == 6 * 9
