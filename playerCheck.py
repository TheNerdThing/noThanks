from player import Player

p = Player()
p.cards.append(1)
p.cards.append(2)
p.cards.append(3)
print(p.cards)
print(p.getScore())