from pokersolver.card import Card, Hand, Rank


def test_rank_gt():
    assert Rank(8) > Rank(6)


def test_card_eq():
    assert Card(8, 1) == Card(8, 1)


def test_hand_eq():
    h1 = Hand(Card(4, 1), Card(5, 1))
    h2 = Hand(Card(5, 1), Card(4, 1))
    assert h1 == h2


def test_hand_neq():
    h1 = Hand(Card(4, 1), Card(5, 1))
    h2 = Hand(Card(4, 1), Card(6, 1))
    assert h1 != h2


def test_hands():
    assert len(Hand.all()) == 1326
