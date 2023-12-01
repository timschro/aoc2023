input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".splitlines()

input = open("day1.txt", 'r')

import re

sum = 0
for line in input:
    numbers = re.findall('[0-9]+', line)
    sum += int(str(numbers[0])[0] + str(numbers[-1])[-1])

print(sum)