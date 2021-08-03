def points(games):
    si = 0
    si = sum(3 if match[0] > match[2] else (1 if match[0] == match[2] else 0) for match in games)
    return si
