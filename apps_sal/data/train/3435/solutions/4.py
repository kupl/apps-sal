import re
le = {"w": 4, "p": 3, "b": 2, "s": 1}
ri = {"m": 4, "q": 3, "d": 2, "z": 1}


def alphabet_war(fight):
    w = re.sub(r"[a-z]\*[a-z]|[a-z]\*|\*[a-z]", "", fight)
    l = sum([le.get(i, 0) for i in w])
    r = sum([ri.get(i, 0) for i in w])
    if l == r:
        return "Let's fight again!"
    return "Right side wins!" if r > l else "Left side wins!"
