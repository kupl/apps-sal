def berserk_rater(a):
    r = 0
    for s in map(str.lower,a):
        if 'clang' in s: r += 5
        elif 'cg' in s: r -=2
        else: r -= 1    
    return 'worstest episode ever' if r<0 else str(r) if 0<=r<=10 else 'bestest episode ever'
