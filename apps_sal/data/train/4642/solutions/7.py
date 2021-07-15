col = {'fire':0,'water':1,'grass':2,'electric':3}
effects = [
    [.5,.5, 2, 1],
    [ 2,.5,.5,.5],
    [.5, 2,.5, 1],
    [ 1, 2, 1,.5]
]
def eff(t1,t2):
    x,y=col[t1],col[t2]
    return effects[x][y]

def calculate_damage(your_type, opponent_type, attack, defense):
    return 50 * (attack / defense) * eff(your_type, opponent_type)
