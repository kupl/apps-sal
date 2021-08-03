def distance(p1, p2):
    return sum((a - b)**2 for a, b in zip(p1, p2))**.5 if p1 and p2 and len(p1) == len(p2) else -1
