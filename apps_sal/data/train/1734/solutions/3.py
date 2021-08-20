class User(object):
    (MAX_RANK, MAX_PROGRESS, DELTA_RANKS) = (8, 100, set(range(-8, 9)) - {0})

    def __init__(self):
        (self.rank, self.progress) = (-8, 0)

    def inc_progress(self, rank):
        if not rank in self.DELTA_RANKS:
            raise ValueError('Invalid value for activity rank')
        dRank = rank - self.rank + (rank * self.rank < 0) * (-1) ** (rank > self.rank)
        self.updateProgress([0, 1, 3, 10 * dRank ** 2][(dRank > -2) + (dRank >= 0) + (dRank > 0)])

    def updateProgress(self, n):
        (nLevel, self.progress) = divmod(self.progress + n, self.MAX_PROGRESS)
        self.rank = min(self.MAX_RANK, self.rank + nLevel + (self.rank + nLevel not in self.DELTA_RANKS))
        if self.rank == self.MAX_RANK:
            self.progress = 0
