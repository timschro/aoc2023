input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".splitlines()

input = open("day4.txt", 'r')

score = 0

def score_card(card):
    matches = 0
    print(card)
    card = card.split(": ",1)[1]
    winning, available = card.split(" | ",1)
    winning= list(filter(None, winning.rstrip().split(" ")))
    available = list(filter(None, available.rstrip().split(" ")))
    print(winning)
    print(available)
    for num in available:
        if num in winning:
            matches += 1
 
    print(matches)
    if matches > 0:
        return pow(2, matches-1)
    else:
        return 0


for card in input:
    score += score_card(card)

print(int(score))
