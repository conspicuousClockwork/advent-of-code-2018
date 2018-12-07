import sys
import functools
from collections import Counter
with open(sys.argv[1], 'r') as f:
    data = f.read().split()


for value, index in enumerate(data):
  print(index)
