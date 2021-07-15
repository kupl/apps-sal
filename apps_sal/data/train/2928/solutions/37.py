def alphabet_war(fight):
    L,R=0,0
    for e in fight:
        if e=='w':L+=4
        if e=='p':L+=3
        if e=='b':L+=2
        if e=='s':L+=1
        if e=='m':R+=4
        if e=='q':R+=3
        if e=='d':R+=2
        if e=='z':R+=1
    if L>R:return "Left side wins!"
    if R>L:return "Right side wins!"
    return "Let's fight again!"
