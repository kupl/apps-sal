class User:

    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, act):
        assert act in range(-8, 0) + range(1, 9)
        diff = act - (act > 0) - self.rank + (self.rank > 0)
        self.progress += (0, 1, 3, diff * diff * 10)[(diff > 0) + (diff >= 0) + (diff >= -1)]
        while self.progress >= 100:
            self.rank += 1 + (self.rank == -1)
            self.progress -= 100
        if self.rank >= 8:
            self.rank, self.progress = 8, 0
