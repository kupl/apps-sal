from string import ascii_uppercase as auc


def quicksum(packet):
    d = {v: k for (k, v) in enumerate(' ' + auc)}
    try:
        return sum((c * d[s] for (c, s) in enumerate(packet, 1)))
    except:
        return 0
