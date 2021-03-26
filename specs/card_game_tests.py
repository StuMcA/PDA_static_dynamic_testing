import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card_1 = Card("hearts", 1)
        self.card_2 = Card("clubs", 10)

    def test_check_for_ace__is_ace(self):
        result = CardGame().check_for_ace(self.card_1)
        self.assertEqual(True, result)

    def test_check_for_ace__is_not_ace(self):
        result = CardGame().check_for_ace(self.card_2)
        self.assertEqual(False, result)

    def test_highest_card__first_higher(self):
        result = CardGame().highest_card(self.card_2, self.card_1)
        self.assertEqual(10, self.card_2.value)
        self.assertEqual("clubs", result.suit)

    def test_highest_card__first_lower(self):
        result = CardGame().highest_card(self.card_1, self.card_2)
        self.assertEqual(10, result.value)
        self.assertEqual("clubs", result.suit)

    def test_cards_total(self):
        cards = [self.card_1, self.card_2]
        result = CardGame().cards_total(cards)
        self.assertEqual("You have a total of 11", result)
