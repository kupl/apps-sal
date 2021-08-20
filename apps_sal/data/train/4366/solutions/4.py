def archers_ready(archers):
    return bool(archers) and all(map(5 .__le__, archers))
