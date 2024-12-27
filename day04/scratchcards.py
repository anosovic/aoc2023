from pathlib import Path
import json
from dataclasses import dataclass
from typing import *
from functools import *
from collections import *

# print(*[ f"{k}: {v}\n" for k,v in Path.__dict__.items() ])

o = lambda x: print(x) or x
def e(x):
    try:
        return x()
    except:
        return None

def input_text():
    p = Path(__file__).parent
    with open(f"{p}/{p.parts[-1]}-input.txt") as f:
        return f.readlines()

@dataclass
class Card:
    num: int
    haves: List[int]
    winning: List[int]

# print(inpinput_textut_text())

def parsed_line(ln) -> Card:
    bfcolon, aftercolon = ln.split(":")
    num = int(bfcolon.split(" ")[-1])
    winn, norm = aftercolon.split("|")
    return Card(
        num,
        [ int(x) for x in norm.split(" ") if e(lambda: int(x))], 
        [ int(x) for x in winn.split(" ") if e(lambda: int(x))]
    )

cards = [parsed_line(x) for x in input_text()]

def numwinning(card: Card):

    return len(set(card.winning) & set(card.haves))

def pointv(n):
    if n == 0:
        return 0
    return 2 ** (n-1)

# print(all(
#     len(set(card.haves)) == len(card.haves)
#     for card in cards
# ))

def partone():
    return sum(
        [
            pointv(numwinning(card))
            for card in cards
        ]
    )

def winningnums(card: Card):
    return set(card.winning) & set(card.haves)

@cache
def card_wins_dict():
    return {
        card.num: winningnums(card)
        for card in cards
    }

@cache
def original_wincount_dict():
    return Counter(card_wins_dict().values())

# number of copies of card = 1 + sum(
#   ( number of copies of prececedent i )
#   for each i
# )

@cache
def precedents():
    toclassify = ( 
        (key, v)
        for key in card_wins_dict()
        for v in card_wins_dict()[key]
    )
    prec = defaultdict(lambda: [])
    [   
        prec[won].append(card)
        for card, won in toclassify
    ]
    return prec

@cache
def howmanyof(i):
    if i not in card_wins_dict():
        return 0
    print(f"{i} has precedents {precedents()[i]} ")
    return 1 + sum(
        howmanyof(p)
        for p in precedents()[i]
    )

def parttwo():
    return sum(
        howmanyof(c)
        for c in card_wins_dict()
    )


print(cards[62])
# print(howmanyof(33))
# print(parttwo())

