class Jack_score(object):

    def __init__(self,  cards):
        self.A     = cards.count('A')
        self.score = sum([int([[e,'10'][e in 'JQK'],'11'][e=='A']) for e in cards])
    
    def get_score(self):
        while self.A and self.score > 21:
                self.score  -= 10
                self.A -= 1
        return self.score
        
def score_hand(c):
    return Jack_score(c).get_score()
