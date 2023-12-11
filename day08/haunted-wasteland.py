import regex

d = {}
with open("day08/input.txt") as f:
  lr = f.readline()
  _ = f.readline()
  while ln := f.readline():
    m = regex.match(r"(\w\w\w) = \((\w\w\w), (\w\w\w)\)", ln)
    if m is None:
      continue
    k, vl, vr = m.captures(1, 2, 3)
    k, vl, vr = k[0], vl[0], vr[0]
    d[k] = (vl, vr)

import itertools

poses = [x for x in d if x[-1] == 'A']
def sim(pos):
  c = 0
  for v in itertools.cycle(lr[:-1]):
    dr = {"L": 0, "R": 1}[v]
    pos = d[pos][dr]
    c += 1
    if pos[-1] == 'Z':
      return c
sims = [sim(pos) for pos in poses]
import math
ans = math.lcm(*sims)
print(ans)

  # print(lr)
