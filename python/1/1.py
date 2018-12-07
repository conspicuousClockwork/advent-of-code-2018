import sys
import functools

with open(sys.argv[1], 'r') as f:
    data = f.read().split()

def preCalibration(frequencies):
    return functools.reduce(lambda a, c : int(a) + int(c), data)

print(preCalibration(data))
