from collections import deque


def who_wins_beggar_thy_neighbour(hand_1, hand_2): return Game(hand_1, hand_2).play()


class Game(object):

    LIMIT, SPECIALS = 10000, {c: n for n, c in enumerate("JQKA", 1)}

    def __init__(self, h1, h2):
        self.count = 0
        self.player = 1
        self.piles = [deque(), deque(h1), deque(h2)]

    def play(self):
        while not self.endGame():
            self.playRound()
        return 2 - self.player if self.count < self.LIMIT else None

    def playRound(self):
        wasPenalty = self.getPenalty()
        for _ in range(wasPenalty or 1):
            self.drawCard()
            if self.endGame() or self.getPenalty():
                break
        else:
            if wasPenalty:
                self.otherGetCommon()
        self.player = 3 - self.player

    def endGame(self): return not self.piles[self.player] or self.count >= self.LIMIT
    def drawCard(self): self.piles[0].append(self.piles[self.player].popleft()); self.count += 1
    def getPenalty(self): return 0 if not self.piles[0] else self.SPECIALS.get(self.piles[0][-1][0], 0)

    def otherGetCommon(self):
        self.piles[3 - self.player].extend(self.piles[0])
        self.piles[0] = deque()
