import random

from numpy import append

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
        
    def show(self):
        print ("{} of {}".format(self.value, self.suit))

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Hearts", "Diamonds"]:
            for v in range(2, 15):
                self.cards.append(Card(s, v))
                # 11 - Jack
                # 12 - Queen
                # 13 - King
                # 14 - Ace

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0 , i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
        
    def drawCard(self):
        return self.cards.pop()

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()
        
    def discard(self):
        return self.hand.pop()

    def trade(self, Player):
        temp = self.hand[0]
        self.hand.clear()
        self.hand.append(Player.hand[0])
        Player.hand.clear()
        Player.hand.append(temp)

deck = Deck()
deck.shuffle()
print("Shuffling...")

order = []

p = Player("Player")
order.append(p)
numBots = 4 #int(input("How many bots?: "))
for i in range(numBots):
    order.append(Player("b" + str(i + 1)))

for x in order:
    x.draw(deck)
    print(x.name + ': ', end ='')
    x.showHand()

for y in order:
    p.trade(y + 1)
    print(x.name + ': ', end ='')
    y.showHand()