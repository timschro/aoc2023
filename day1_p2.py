input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".splitlines()

input = open("day1.txt", 'r')

import re

replace = "zero one two three four five six seven eight nine".split()

sum = 0
for line in input:
    tuples = []
    for number in replace:
        index = line.find(number)
        if index > -1:
            tuples.append([index, number])
    tuples = sorted(tuples)
    for t in tuples:
        line = line.replace(t[1], t[1]+str(replace.index(t[1]))+t[1])
    numbers = re.findall('[0-9]+', line)
    sum += int(str(numbers[0])[0] + str(numbers[-1])[-1])

print(sum)