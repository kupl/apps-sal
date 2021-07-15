def berserk_rater(l):
    score = 0
    for i in l:
        if 'cg' in i.lower() and 'clang' in i.lower(): score += 5
        elif 'clang' in i.lower(): score += 5
        elif 'cg' in i.lower(): score -= 2
        else: score -= 1
    
    if score < 0: return 'worstest episode ever'
    elif score > 10: return 'bestest episode ever'
    else: return str(score)
