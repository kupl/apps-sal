def beasts(heads, tails):
    h = (heads-tails*2)/3
    if h<0 or tails-h<0: return "No solutions"
    return [tails-h, h]
