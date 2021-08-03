class User:
    ranks = range(-8, 0) + range(1, 9)

    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, rank):
        if rank not in User.ranks:
            raise ValueError('Invalid rank')
        d = User.ranks.index(rank) - User.ranks.index(self.rank)
        p = 0 if d < -1 else (
            1 if d == -1 else (
                3 if d == 0 else 10 * d * d))
        r = int((self.progress + p) / 100)
        r = User.ranks.index(self.rank) + r
        self.rank = User.ranks[r if r < len(User.ranks) else -1]
        self.progress = (self.progress + p) % (100 if self.rank < User.ranks[-1] else 1)
