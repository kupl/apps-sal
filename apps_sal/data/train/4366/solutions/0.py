def archers_ready(archers):
    return all((i >= 5 for i in archers)) if archers else False
