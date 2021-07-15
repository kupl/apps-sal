def alphabet_war(fight):
    l = 0
    r = 0
    right = {'m':4,'q':3,'d':2,'z':1}
    left = {'w':4,'p':3,'b':2,'s':1}
    for i in fight:
        if i in right:
            r += right[i]
        elif i in left:
            l += left[i]
    if l > r:
        return "Left side wins!"
    elif r > l:
        return "Right side wins!"
    else:
        return "Let's fight again!"
