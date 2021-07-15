def archers_ready(archers):
    return archers != [] and all(x > 4 for x in archers)
