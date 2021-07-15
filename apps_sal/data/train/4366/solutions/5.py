def archers_ready(archers):
    return all(n >= 5 for n in archers) if archers else False
