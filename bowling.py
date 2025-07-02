def scoreRolls(rolls):
    return sum(rolls)


gametests = [
    [[0,0,0,0,0,0,0,0,0,0], 0],
    [[9,9,9,9,9,9,9,9,9,9], 90]
]

for rolls, expectedScore in gametests:
    actualScore = scoreRolls(rolls)
    if actualScore != expectedScore:
        print('rolls:', rolls, 'scored', actualScore, 'but expected', expectedScore)

