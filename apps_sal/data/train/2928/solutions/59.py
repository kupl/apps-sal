def alphabet_war(fight):
    lef = {"w" : 4, "p" : 3, "b" : 2, "s" : 1}
    rig = {"m" : 4, "q" : 3, "d" : 2, "z" : 1}
    lp = 0
    rp = 0
    for x in fight:
        if x in lef:
            lp += lef[x]
        if x in rig:
            rp += rig[x]
    return "Right side wins!" if rp > lp else "Left side wins!"if lp > rp else "Let's fight again!"
