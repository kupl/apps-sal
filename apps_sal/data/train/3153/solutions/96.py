def playerRankUp(pts):
    return False if Player(pts).rank < 100 else 'Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up.'


class Player(object):

    def __init__(self, rank):
        self.rank = rank
