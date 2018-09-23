from cards import Hand, Deck, Pile, Card
from typing import Dict
from copy import copy

jack  = 11
queen = 12
king  = 13
ace   = 14

high_card = 1
pair      = 2
two_pair  = 3
three     = 4
straight  = 5
flush     = 6
full_house= 7
four      = 8
straight_flush = 9
royal     = 9

def is_number(c: Card,number:int)->bool:
    return c.number == number

def is_suit(c: Card,suit:int)->bool:
    return c.suit == suit

def has_number(h: Pile, number:int)->int:
    for i,card in enumerate(h):
        if is_number(card,number):
            return i
    return -1

def has_suit(h: Pile, suit:int)->bool:
    for card in h:
        if card.suit == suit:
            return True
    return False

def kelly(b,p):
    """calculates the portfolio fraction to bet from
       the kelly criterion"""
    return ((b*p)-(1.-p))/b

def is_flush(hand: Hand)->bool:
    suit = hand[0].suit
    for card in hand:
        if card.suit != suit:
            return False
    return True

def pairs(h: Hand)->Dict[Card,int]:
    hand = copy(h)
    out = {}
    while hand != []:
        card = hand.pop()
        out[card] = 1
        hn = has_number(hand,card.number)
        while hn != -1:
            out[card]+=1
            hand.pop(hn)
            hn = has_number(hand,card.number)
    return out

def which_hand(h: Hand)->int:
    hand = copy(h)
    prs = pairs(hand)
    prs = [prs[k] for k in prs]
    if prs.count(4) == 1:
        return four
    if prs.count(3) == 1 and prs.count(2) != 1 :
        return three
    if prs.count(2) == 1 and prs.count(3) == 1:
        return full_house
    if prs.count(2) == 2:
        return two_pair
    if prs.count(2) == 1:
        return pair
    if is_flush(hand):
        return flush
    

