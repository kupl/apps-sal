def quicksum(p):
    return sum((i * (ord(e) - 64) * (e != ' ') for (i, e) in enumerate(p, 1))) * all((x in __import__('string').ascii_uppercase + ' ' for x in p))
