def scoreGame(rolls):
    return sum(rolls)


class Frame:
    def __init__(self):
        self.rolls = []

    def addRoll(self, roll):
        self.rolls.append(roll)

    def score(self):
        return sum(self.rolls)


frametests = [
    ['bad frame', [0,0], 0]
]

for scenario, rolls, expectedScore in frametests:
    frame = Frame()
    for roll in rolls:
        frame.addRoll(roll)

    actualScore = frame.score()
    if actualScore != expectedScore:
        print('scenario: "', scenario, '" scored', actualScore, 'but expected', expectedScore)


gametests = [
    ['bad game', [0,0,0,0,0,0,0,0,0,0], 0],
    ['ok game', [9,9,9,9,9,9,9,9,9,9], 90],
    # ['score a spare', [9,1,5,0,0,0,0,0,0,0], 20],
]

for scenario, rolls, expectedScore in gametests:
    actualScore = scoreGame(rolls)
    if actualScore != expectedScore:
        print('scenario: "', scenario, '" scored', actualScore, 'but expected', expectedScore)

