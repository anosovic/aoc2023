from inspect import currentframe as cf
from pointfree import *
from operator import *
from pathlib import Path
import re
from itertools import *
from functools import *

@pf
def id(x):
    return x

@pf
def out(x):
    print(x)
    return x

def sample():
    return [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen"
    ]

@pf
def inputtxt():
    with open(f"{Path(__file__).parent}/input.txt") as f:
        return [line.rstrip() for line in f.readlines()]

@pf
def subwords(ln):
    words = { 
        v: str(i+1) for i,v in enumerate([
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine"
        ]) 
    }
    return re.sub(
        rf"({'|'.join(words)})", 
        lambda m: words[m.group(1)], 
        ln
    ) + re.sub(
        rf"({'|'.join([word[::-1] for word in words])})", 
        lambda m: words[m.group(1)[::-1]][::-1], 
        ln[::-1]
        
    )[::-1]

@pf
def firstlast(s):
    d = (pfmap(str) >> pfcollect)(range(10))
    k = [x for x in s if x in d]
    return (int(''.join([k[0], k[-1]])))

def result():
    # return (
    #     inputtxt >> pfmap(subwords) \
    #         >>  pfmap(firstlast) >> pf(sum)
    # )()
    strs = [
        [
            c
            for c in subwords(ln) 
            if c in map(str,range(1,10))
         ] for ln in inputtxt() 
    ]
    ints = [
        int(s[0] + s[-1])
        for s in strs
    ]
    return sum(ints)
        


result()