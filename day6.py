#Example input
input = """Time:      7  15   30\nDistance:  9  40  200"""

#Real input
input = """Time:        40     81     77     72\nDistance:   219   1012   1365   1089"""

#part 2 only
input = input.replace(" ", "")

input = input.splitlines()

import re
from functools import reduce

times = re.findall('[0-9]+', input[0])
times = list(map(int, times))
distances = re.findall('[0-9]+', input[1])
distances = list(map(int, distances))
wins_overall = []
for i in range(len(distances)):
    time = times[i]
    distance = distances[i]
    wins = travel = 0
    for duration in range(time):
        travel = duration * (time - duration)
        if travel > distance:
            wins+=1
    wins_overall.append(wins)

print(reduce((lambda x, y: x * y), wins_overall))