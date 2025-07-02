import unittest

def scoreGame(rolls):
    return sum(rolls)


class Frame:
    def __init__(self):
        self.rolls = []

    def addRoll(self, roll):
        self.rolls.append(roll)

    def score(self):
        return sum(self.rolls)

class BowlingTest(unittest.TestCase):
    
    def test_score_bad_frame(self):
        badFrame = Frame()
        badFrame.addRoll(0)
        badFrame.addRoll(0)
        self.assertEqual(0, badFrame.score(), 'Rolled zeros, score should be zero')

    def test_score_good_frame(self):
        badFrame = Frame()
        badFrame.addRoll(4)
        badFrame.addRoll(5)
        self.assertEqual(9, badFrame.score(), 'Rolled four and five, score shiould be nine')

if __name__ == '__main__':
    unittest.main()
