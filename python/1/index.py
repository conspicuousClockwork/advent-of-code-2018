import sys
import functools
from problemInput import data

# Use reduce to parse all input values and return a sum
print(functools.reduce(lambda a, c : int(a) + int(c), data))
    
