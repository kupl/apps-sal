def archers_ready(archers):
    return len(archers) > 0 and all(a > 4 for a in archers)
