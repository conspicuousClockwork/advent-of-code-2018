import sys
import functools
from collections import Counter
with open(sys.argv[1], 'r') as f:
    data = f.read().split()

def checkSum(inventory):
    twos = 0
    threes = 0
    for id in inventory:
        counted = Counter(list(id))
        three = False
        two = False
        for key, value in counted.items():
            if value == 2 and not two:
                twos = twos + 1
                two = True
            if value == 3 and not three:
                threes = threes + 1
                three = True
            if two and three:
                break

    return twos * threes
            
print(checkSum(data))
