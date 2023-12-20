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
from collections import *
from textwrap import dedent

@pf
def id(x):
    return x

@pf
def out(x):
    print(x)
    return x

@cache
def sample():
    return dedent("""
        467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598..
    """).split("\n")

@cache
def inputtxt():
    with open(f"{Path(__file__).parent}/input.txt") as f:
        return [line.rstrip() for line in f.readlines()]

@cache
def nums():
    return set(pfmap(str, range(10)))

@cache
def assignment(ln):
    # classify by index of first number in series
    d = [ 0 if ln[0] in nums() else '.' ] * len(ln)
    for i in range(1, len(ln)):
        d[i] = ( 
            (d[i-1] if d[i-1] != '.' else i)
            if ln[i] in nums()
            else '.'
        )
    
    d2 = defaultdict(lambda: [])
    for i,v in enumerate(d):
        d2[v].append(i)
    
    # voila!
    return { 
        u+a: (u, int(w)) # classify, value
        for u,w in (
            (i, "".join(ln[z] for z in v))
            for i,v in d2.items()
            if i != '.'
        )
        for a,c in enumerate(w)
    }

@cache
def dirs():
    return [
        (u,v) 
        for u,v in product(range(-1,2), range(-1,2))
        if (u,v) != (0,0)
    ]

def part1():
    data = inputtxt()
    stuff = chain(*[ 
        [
            # reclassify based on both row and starting column 
            ( (newr, asgn[newc][0]), asgn[newc][1] )
            for newr,newc in [ 
                ( pf(starmap) >> pf(tuple)) (add, zip(dir,(row,col))) 
                for dir in dirs() 
            ]
            if newr < len(data)
            for asgn in [ assignment(data[newr]) ]
            if newc in asgn
        ] 
        for row,ln in enumerate(data)
        for col, c in enumerate(ln)
        if c not in nums() and c != '.' 
    ])
    return sum(dict(stuff).values())

def part2():
    data = inputtxt()
    stuff2 = [ 
        pfreduce(mul, reclas.values()) 
        for row,ln in enumerate(data)
        for col, c in enumerate(ln)
        if c == '*'
        for reclas in [ dict([
            # reclassify based on both row and starting column 
            ( (newr, asgn[newc][0]), asgn[newc][1] )
            for newr,newc in [ 
                ( pf(starmap) >> pf(tuple)) (add, zip(dir,(row,col))) 
                for dir in dirs() 
            ]
            if newr < len(data)
            for asgn in [ assignment(data[newr]) ]
            if newc in asgn
        ]) ] 
        if len(reclas) == 2
    ]
    return sum(stuff2)

part1()
part2()