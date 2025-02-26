players = []
numPlayers = 5
# numPlayers = int(input("how many players: ")

    
showPlayers(players)
while upCard != -1:
    upCard = drawCard(deck)
    print("the up card is: " ,upCard)
    option = int(input("will turn player take or pass?(1 for take 0 for pass): "))
    if option == 0:
        if canPass(players[turnPlayer], numPlayers):
            
        
        
    