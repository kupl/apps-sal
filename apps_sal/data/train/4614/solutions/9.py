class eater:
    
    def __init__(self, dict):
        self.name = dict['name']
        self.chickenwings = dict['chickenwings'] if 'chickenwings' in dict.keys() else 0
        self.hamburgers = dict['hamburgers'] if 'hamburgers' in dict.keys() else 0
        self.hotdogs = dict['hotdogs'] if 'hotdogs' in dict.keys() else 0
        
    def score(self):
        return 5*self.chickenwings + 3*self.hamburgers + 2*self.hotdogs

def scoreboard(who_ate_what):
    score = []
    for D in who_ate_what:
        score.append({'name': D['name'], 'score': eater(D).score()})
    return sorted(score, key = lambda x: (-x['score'], x['name']))
