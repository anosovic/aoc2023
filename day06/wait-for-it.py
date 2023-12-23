from pathlib import Path
import json
from dataclasses import dataclass
from typing import *
from functools import *
from itertools import *

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
class race:
    time: int
    distance: int

def parse(lines):
    numbers = [
        [ 
            int(x) 
            for x in line.split(":")[1].strip().split(" ") 
            if e(lambda: int(x)) 
        ]
        for line in lines
    ]
    return list(starmap(race, zip(*numbers)))

# print(parse(input_text()))

# (t-x) * x = d
# -x^2 + tx - d = 0
# x^2 -tx + d = 0
# ( -b +- sqrt(b^2-4ac) ) / 2a
# 