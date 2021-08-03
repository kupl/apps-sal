def alphabet_war(fight):
    a = list()
    b = list()
    left = dict(list(zip('wpbs', [4, 3, 2, 1])))
    right = dict(list(zip('mqdz', [4, 3, 2, 1])))
    for i in fight:
        if i == "w" or i == "p" or i == "b" or i == "s":
            a.append(left[i])
        elif i == "m" or i == "q" or i == "d" or i == "z":
            b.append(right[i])
    if sum(b) > sum(a):
        return "Right side wins!"
    elif sum(a) > sum(b):
        return "Left side wins!"
    else:
        return "Let's fight again!"
