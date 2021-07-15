def distribution_of(golds):
    p,g,player=0,golds[:],[0,0]
    while g: player[p],p = player[p]+g.pop(-1 if g[0]<g[-1] else 0),1-p
    return player
