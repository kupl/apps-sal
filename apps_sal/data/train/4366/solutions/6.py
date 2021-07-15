def archers_ready(archers):
    return bool(archers) and all(x >= 5 for x in archers)
