import sys

with open(sys.argv[1], 'r') as f:
    data = f.read().split()

def calibrate(inputFrequencies):
    frequencies = {0}
    currentFrequency = 0

    while(True):
        for delta in inputFrequencies:
            currentFrequency = currentFrequency + int(delta)
            if currentFrequency in frequencies:
                print(currentFrequency)
                exit()

            frequencies.add(currentFrequency)

print(calibrate(data))
