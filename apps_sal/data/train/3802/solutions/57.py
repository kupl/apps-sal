def hoop_count(n):
    encourage = {1: 'Great, now move on to tricks', 0: 'Keep at it until you get it'}
    return encourage.get(n >= 10)
