import random

class Deck:
    
    def __init__(self):
        self.cards = []
        for i in range(3,35):
            self.cards.append(i)
        random.shuffle(self.cards)
        self.cards = self.cards[9:]
       
    #will return -1 when the deck is out of cards
    def draw(self):
        if len(self.cards) == 0:
            return -1
        give = self.cards[0]
        self.cards = self.cards[1:]
        return give