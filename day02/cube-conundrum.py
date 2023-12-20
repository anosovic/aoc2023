from inspect import currentframe as cf
from pointfree import *
from operator import *
from pathlib import Path
import re
from itertools import *
from functools import *
from dataclasses import *
from typing import *
from enum import *

@pf
def id(x):
    return x

@pf
def out(x):
    print(x)
    return x

@pf
def inputtxt():
    with open(f"{Path(__file__).parent}/input.txt") as f:
        return [line.rstrip() for line in f.readlines()]

@dataclass
class Round:
    r: int
    g: int
    b: int

@dataclass
class Game:
    no: int
    rounds : List[Round]

@pf
def parse(ln):
    game,rest = ln.split(": ")
    gameno = int(game.split(" ")[1])
    parsedrounds = [
        Round(**(
            dict(product(
                ["r", "g", "b"],
                [0] * 3
            )) | {
                countrecord[1][0]: int(countrecord[0])
                for cubecount in round.split(", ")
                for countrecord in [cubecount.split(" ")]
            }
        ))
        for round in rest.split("; ")
    ]
    return Game(gameno, parsedrounds)

def allgames():
    return [ 
        parse(game) for game in inputtxt() 
    ]

def islegal(game: Game):
    maxr, maxg, maxb = 12, 13, 14
    legality = [
        round.r <= maxr and \
            round.g <= maxg and \
            round.b <= maxb
        for round in game.rounds
    ]
    return all(legality)

def part1():
    return sum([ 
        game.no
        for game in allgames() 
        if islegal(game) 
    ])

def mincubes(game):
    rs = max([ round.r for round in game.rounds ])
    gs = max([ round.g for round in game.rounds ])
    bs = max([ round.b for round in game.rounds ])
    return [rs,gs,bs]

def part2():
    return sum(
        pfreduce(mul,mincubes(game))
        for game in allgames()
    )

part1()
part2()