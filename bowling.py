import unittest
from functools import reduce

class Frame:
    def __init__(self):
        self.rolls = []

    def roll(self, roll):
        self.rolls.append(roll)

    def score(self):
        return sum(self.rolls)

    def isOpen(self):
        if len(self.rolls) < 2:
            return True

        if self.isSpare() and len(self.rolls) < 3:
            return True

        if self.isStrike() and len(self.rolls) < 3:
            return True

        return False

    def shouldStartNextFrame(self):
        if len(self.rolls) > 1:
            return True

        if self.isSpare():
            return True

        if self.isStrike():
            return True

    def isStrike(self):
        return len(self.rolls) > 0 and self.rolls[0] == 10

    def isSpare(self):
        return len(self.rolls) > 1 and self.rolls[0] + self.rolls[1] == 10


class Game:
    def __init__(self):
        self.frames = []
        self.currentFrameIdx = 0

        for i in range(10):
            self.frames.append(Frame())

    def roll(self, pinsDown):
        for frame in self.openFrames():
            frame.roll(pinsDown)

        if self.shouldStartNextFrame():
            self.startNextFrame()

    def score(self):
        return reduce(
            lambda carry, frame: carry + frame.score(),
            self.frames,
            0
        )
            
    def openFrames(self):
        return filter(
            lambda frame: frame.isOpen(),
            self.frames[:self.currentFrameIdx + 1]
        )

    def startNextFrame(self):
        self.currentFrameIdx += 1

    def shouldStartNextFrame(self):
        if not self.frames[self.currentFrameIdx].shouldStartNextFrame():
            return False

        if self.currentFrameIdx == len(self.frames) - 1:
            return False

        return True


class FrameTest(unittest.TestCase):
    
    def test_score_bad_frame(self):
        badFrame = Frame()
        badFrame.roll(0)
        badFrame.roll(0)
        self.assertEqual(0, badFrame.score(), 'Rolled zeros, score should be zero')

    def test_score_good_frame(self):
        goodFrame = Frame()
        goodFrame.roll(4)
        goodFrame.roll(5)
        self.assertEqual(9, goodFrame.score(), 'Rolled four and five, score should be nine')

    def test_score_spare(self):
        spareFrame = Frame()
        spareFrame.roll(5)
        spareFrame.roll(5)
        self.assertTrue(spareFrame.isOpen(), 'frame should still be open after a spare')
        spareFrame.roll(5)
        self.assertEqual(15, spareFrame.score(), 'rolled three fives, score should be fifteen')
        self.assertFalse(spareFrame.isOpen(), 'spare frame should be closed after third roll')

    def test_score_strike(self):
        strikeFrame = Frame()
        strikeFrame.roll(10)
        self.assertTrue(strikeFrame.isOpen(), 'frame should still be open after a strike')
        strikeFrame.roll(5)
        self.assertTrue(strikeFrame.isOpen(), 'frame should still be open after a strike and first bonus')
        strikeFrame.roll(5)
        self.assertEqual(20, strikeFrame.score(), 'rolled ten and two fives, score should be twenty')
        self.assertFalse(strikeFrame.isOpen(), 'strike frame should be closed after third roll')

    def test_should_open_next_frame_after_two_rolls(self):
        twoRollFrame = Frame()
        self.assertFalse(twoRollFrame.shouldStartNextFrame(), 'next frame should not be open before any rolls')
        twoRollFrame.roll(4)
        self.assertFalse(twoRollFrame.shouldStartNextFrame(), 'next frame should not be open after one roll')
        twoRollFrame.roll(4)
        self.assertTrue(twoRollFrame.shouldStartNextFrame(), 'next frame should open after two rolls')

    def test_should_open_next_frame_after_spare(self):
        spareFrame = Frame()
        spareFrame.roll(5)
        self.assertFalse(spareFrame.shouldStartNextFrame(), 'next frame should not be open after one roll')
        spareFrame.roll(5)
        self.assertTrue(spareFrame.shouldStartNextFrame(), 'next frame should open after spare')

    def test_should_open_next_frame_after_strike(self):
        strikeFrame = Frame()
        strikeFrame.roll(10)
        self.assertTrue(strikeFrame.shouldStartNextFrame(), 'next frame should open after strike')


class GameTest(unittest.TestCase):

    def test_score_bad_game(self):
        game = Game()
        for i in range(20):
            game.roll(0)

        self.assertEqual(0, game.score(), 'bad game should score zerro')

    def test_score_ok_game(self):
        game = Game()
        for i in range(20):
            game.roll(4)

        self.assertEqual(80, game.score(), 'ok game should score ninety')

    def test_score_spare(self):
        game = Game()
        game.roll(5)
        game.roll(5)
        game.roll(5)

        self.assertEqual(20, game.score(), 'spare should give 10 + bonus')

    def test_score_strike(self):
        game = Game()
        game.roll(10)
        game.roll(10)
        game.roll(10)

        self.assertEqual(60, game.score(), 'strike should give 10 + two bonuses')

    def test_perfect_game(self):
        game = Game()
        for i in range(13):
            game.roll(10)

        self.assertEqual(300, game.score(), 'perfect game should be 300')

    def test_all_spares(self):
        game = Game()
        for i in range(21):
            game.roll(5)

        self.assertEqual(150, game.score(), 'all spares should be 150');

if __name__ == '__main__':
    unittest.main()
