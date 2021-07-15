def shoot(results):
    pt1, pt2 = 0, 0
    countPts = lambda elt,pt: (elt[1]+1)*elt[0][pt].count('X')
    for elt in results:
        pt1 += countPts(elt,'P1')
        pt2 += countPts(elt,'P2')
    if pt1>pt2 :     return 'Pete Wins!'
    elif pt1==pt2 :  return 'Draw!'
    else:            return 'Phil Wins!'
