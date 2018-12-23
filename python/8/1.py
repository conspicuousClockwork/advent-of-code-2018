import sys
import functools
from collections import OrderedDict

with open(sys.argv[1], 'r') as f:
    data = map(lambda x : int(x), f.read().split())

print(data)

tree = {
    'cl': data[0],
    'ml': data[1],
    'data': data[2:],
    'children': [],
    'meta': [],
}

while True:
    
