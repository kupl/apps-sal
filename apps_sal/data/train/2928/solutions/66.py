def alphabet_war(fight):
    res = 0
    right = ' zdqm'
    left = ' sbpw'
    for i in fight:
        try:
            res -= left.index(i)
        except:
            try:
                res += right.index(i)
            except:
                pass
    if res > 0:
        return 'Right side wins!'
    if res == 0:
        return "Let's fight again!"
    return 'Left side wins!'
