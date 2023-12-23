from pathlib import Path
import json
from dataclasses import dataclass
from typing import *

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

print(input_text())