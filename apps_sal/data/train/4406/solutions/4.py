from itertools import accumulate as acc

def tram(stops, down, up):
    return max(acc(u - d for d, u in zip(down[:stops], up)))
