"""My attempt at building a blackjackish game"""

from random import randint


class Card:

    def __init__(self, face, suit):
        self._suit = suit
        self._face = face

    def __str__(self):
        return f'{self._face} Of {self._suit}'

    @property
    def suit(self):
        return self._suit

    @property
    def face(self):
        return self._face


class Deck:

    def __init__(self, cards):
        self._cards = cards

    def __str__(self):
        listofcards = ''
        for card in self._cards:
            listofcards += str(card) + '\n'
        return listofcards

    def getcard(self, index):
        return self._cards[index]

    def getlength(self):
        return len(self._cards)

    def shuffle(self):
        for x in range(0, len(self._cards) - 1):
            swapId = randint(0, len(self._cards) - 1)
            temp = self._cards[swapId]
            self._cards[swapId] = self._cards[x]
            self._cards[x] = temp

    def dealacard(self):
        return self._cards.pop()




class Player:

    def __init__(self, name):
        self._name = name
        self._hand = []
        self._score = 0

    def calcScore(self):
        score = 0
        if self._hand:
            for iter in self._hand:
                if iter.face == '2':
                    score += 2
                elif iter.face == '3':
                    score += 3
                elif iter.face == '4':
                    score += 4
                elif iter.face == '5':
                    score += 5
                elif iter.face == '6':
                    score += 6
                elif iter.face == '7':
                    score += 7
                elif iter.face == '8':
                    score += 8
                elif iter.face == '9':
                    score += 9
                else:
                    score += 10
        if score < 21 and self.hasAce():
            score += 1
        self._score = score

    def getCard(self, card):
        self._hand.append(card)

    def __str__(self):
        myhand = ''
        for card in self._hand:
            myhand +=str(card) + '\n'
        return f'Player: {self._name} \n' \
               f'Hand: {myhand}' \
               f'Score: {self._score}'

    def hasAce(self):
        for card in self._hand:
            if card.face == 'Ace':
                return True

    @property
    def score(self):
        return self._score




s = 'Hearts', 'Diamonds', 'Clovers', 'Spades'
f = '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'

d = [Card(j, i) for i in s for j in f]

deck = Deck(d)

deck.shuffle()
deck.shuffle()

p = Player('Shaan')
d = Player('Dealer')

p.getCard(deck.dealacard())
d.getCard(deck.dealacard())
p.getCard(deck.dealacard())
d.getCard(deck.dealacard())


p.calcScore()
d.calcScore()

print(p)
print(d)

while p.score <= 21:
    check = input('Hit?')
    if check == 'Y':
        p.getCard(deck.dealacard())
        p.calcScore()
        print(p)




