def alphabet_war(fight):
    sides, winer = { 'w':-4,'p':-3,'b':-2,'s':-1 , 'm':4, 'q':3, 'd':2, 'z':1 }, 0
    for e in fight:  winer += sides.get( e, 0 )
    return ["Let's fight again!",'Right side wins!','Left side wins!'][(winer>=0) - (winer<=0)]

