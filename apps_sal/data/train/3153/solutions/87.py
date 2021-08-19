class Player(object):

    def __init__(self, pts, rank='E5'):
        self.rank = rank
        self.pts = pts

    def check(self):
        if self.pts < 100:
            return False
        else:
            return 'Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up.'


def playerRankUp(pts):
    return Player(pts).check()
