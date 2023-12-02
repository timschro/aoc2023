input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".splitlines()

input = open("day2.txt", 'r')

import re

available = {"red": 12, "green": 13, "blue": 14}

games = []
powers = []

for line in input:
    reds = re.findall(r'\d+ red', line)
    reds = [int(re.findall(r'\d+', element)[0]) for element in reds]
    blues = re.findall(r'\d+ blue', line)
    blues = [int(re.findall(r'\d+', element)[0]) for element in blues]
    greens = re.findall(r'\d+ green', line)
    greens = [int(re.findall(r'\d+', element)[0]) for element in greens]
    powers.append(max(reds)*max(blues)*max(greens))
    
    valid = True
    for red in reds:
        if red > available["red"]:
            valid = False
    for blue in blues:
        if blue > available["blue"]:
            valid = False
    for green in greens:
        if green > available["green"]:
            valid = False
    if valid:
        game = re.findall(r'\d+', line)
        games.append(int(game[0]))

print(sum(games))
print(sum(powers))
   




