class Player:
    def __init__(self):
        self.stones = 11
        self.cards = []
        
    def getScore(self):
        if len(self.cards) == 0:
            return 0
        self.cards.sort()
        scoreingCards= [self.cards[0]]
        score = 0
        sequenceLength = 1
        for x in self.cards[1:]:
            if x != scoreingCards[-1] +sequenceLength :
                scoreingCards.append(x)
                sequenceLength = 1
            else:
                sequenceLength += 1
        for i in scoreingCards:
            score += i
        return score
    