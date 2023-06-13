import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("Hearts",7)
        self.card2 = Card("Clubs", 11)
        self.card3 = Card("Diamonds", 1)
        self.card4 = Card("Spades",12)
        self.cardGame = CardGame(self.card3)
        self.cards = [self.card1,self.card2,self.card3,self.card4]


    def test_check_for_ace(self):
        self.assertEqual(True, self.cardGame.check_for_ace(self.card3))

    def test_highestCard(self):
        self.assertEqual(self.card2,self.cardGame.highest_card(self.card1,self.card2))

    def test_cards_total(self):
        self.assertEqual("You have a total of 31", self.cardGame.cards_total(self.cards))