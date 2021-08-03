import string


def alphabet_war(fight):
    leftside = [x for x in fight.lower() if x in "wpbs"]
    rightside = [x for x in fight.lower() if x in "mqdz"]
    rl = sum(int(x) for x in "".join(leftside).translate(str.maketrans("wpbs", "4321")))
    rr = sum(int(x) for x in "".join(rightside).translate(str.maketrans("mqdz", "4321")))
    if rl == rr:
        return "Let's fight again!"
    elif rl > rr:
        return "Left side wins!"
    else:
        return "Right side wins!"
