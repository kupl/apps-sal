class User(object):
    def __init__(self):
        self.ranks, self.cur_rank, self.progress = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8], 0, 0

    def get_rank(self):
        return self.ranks[self.cur_rank]

    def set_rank(self, arg):
        '''Nope'''
    rank = property(get_rank, set_rank)

    def inc_progress(self, k_rank):
        k_rank = self.ranks.index(k_rank)
        if self.rank == 8:
            return
        if k_rank == self.cur_rank:
            self.progress += 3
        elif k_rank == self.cur_rank - 1:
            self.progress += 1
        elif k_rank > self.cur_rank:
            diff = k_rank - self.cur_rank
            self.progress += 10 * diff * diff
        while self.progress >= 100:
            self.cur_rank += 1
            self.progress -= 100
            if self.rank == 8:
                self.progress = 0
                return
