def alphabet_war(fight):
    dl={"w":4,"p":3,"b":2,"s":1}
    dr={"m":4,"q":3,"d":2,"z":1}
    lwork=0
    rwork=0
    for x in fight:
        lwork+=dl.get(x,0)
        rwork+=dr.get(x,0)
    if lwork==rwork : return "Let's fight again!"
    elif lwork>rwork : return "Left side wins!"
    else : return "Right side wins!"
