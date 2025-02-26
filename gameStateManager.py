from player import Player
from deck import Deck

def class GameState:
    
    def __init__(self,numPlayers):
        self.turnPlayer = 0
        self.players = []
        self.deck = Deck()
        self.upCard = 0
        for x in range(0,numPlayers):
            self.players.append(Player())
        
    def showPlayers(players):  
        for player in players:
            print(player, "has ", player.stones, " stones")
            print(player, "has ", player.getScore(), " points")

    def drawCard(deck):
        return deck.draw()
        
    def nextTurn(index, numPlayerss):
        if index + 1  < numPlayers:
            return index+=1
        else: 
            return 0
        
    def canPass(player):
        return player.stones>0