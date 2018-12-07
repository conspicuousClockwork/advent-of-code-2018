import sys
import functools
from collections import Counter
with open(sys.argv[1], 'r') as f:
    data = f.read().split()

def string_pop(s, i):
    l = list(s)
    l.pop(i)
    return ''.join(l)

def findStringNeighbor(inventory):
    id_length = len(inventory[0])
    for i in range(id_length):
        popped = list(map(lambda box_id: string_pop(box_id, i), inventory))
        if len(inventory) != len(set(popped)):
            for box_id, value in Counter(popped).items():
                if value > 1:
                    return box_id

print(findStringNeighbor(data))
