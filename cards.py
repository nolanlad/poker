from typing import List
from random import shuffle


def suit_as_str(suit:int)->str:
    if suit == 0:
        return 'clubs'
    elif suit == 1:
        return 'diamonds'
    elif suit == 2:
        return 'hearts'
    elif suit == 3:
        return 'spades'

def number_as_str(number:int)->str:
    if number > 1 and number < 11:
        return str(number)
    else:
        if number == 11:
            return 'jack'
        if number == 12:
            return 'queen'
        if number == 13:
            return 'king'
        if number == 1 or number == 14:
            return 'ace'


class Card:
    def __init__(self, suit: int, number: int):
        self.suit = suit
        self.number = number
    def __eq__(self,other) -> bool:
        return self.suit == other.suit and self.number == other.number
    def __lt__(self,other):
        if other.number == self.number:
            return other.suit < self.suit
        else:
            return other.number < self.number
    def __str__(self):
        return "%s of %s"%(number_as_str(self.number),suit_as_str(self.suit))
    def __repr__(self):
        return self.__str__()
    def __hash__(self):
        return hash(str(self.suit)+str(self.number))
    
        
class Pile(list):
    def __init__(self,cards: List[Card]):
        super().__init__(cards)

class Deck(Pile):
    def __init__(self):
        cards = []
        for i in range(2,15):
            for j in range(0,4):
                c = Card(j,i)
                cards.append(c)
        super().__init__(cards)
        self.shuffle()
    def shuffle(self)->None:
        shuffle(self)

class Hand(Pile):
    def __init__(self):
        super().__init__([])
    def draw(self,other:Deck):
        for i in range(5):
            self.append(other.pop())
        self.sort()
            

