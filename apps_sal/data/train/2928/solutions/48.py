def alphabet_war(fight):
    l_scores = {"w": 4, "p": 3, "b": 2, "s": 1}
    r_scores = {"m": 4, "q": 3, "d": 2, "z": 1}
    l = 0
    r = 0
    for ch in fight:
        l += (l_scores[ch] if ch in list(l_scores.keys()) else 0)
        r += (r_scores[ch] if ch in list(r_scores.keys()) else 0)
    return ("Left side wins!" if l>r 
           else "Right side wins!" if r>l
           else "Let's fight again!")

