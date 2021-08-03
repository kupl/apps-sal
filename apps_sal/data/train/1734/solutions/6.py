class User():
    '''Creates a User class for a codewars style website'''

    def __init__(self):
        self.ranks = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]  # 15
        self.progress = 0
        self.level = 0
        self.rank = self.ranks[self.level]

    def inc_progress(self, rank):

        if rank not in self.ranks:
            raise Exception('Invalid rank')

        activityrank = self.ranks.index(rank)
        rank = self.level
        difference = activityrank - rank

        if self.level < 15:

            if difference > 0:
                points = 10 * difference * difference
                self.progress += points

            elif difference == 0:
                self.progress += 3

            elif difference == -1:
                self.progress += 1

            if self.progress == 100:
                self.level += 1
                self.rank = self.ranks[self.level]
                self.progress = 0

            while self.progress >= 100:
                self.level += 1
                leftover = self.progress - 100
                self.rank = self.ranks[self.level]

                if self.level < 15:
                    self.progress = leftover

                elif self.level >= 15:
                    self.progress = 0
