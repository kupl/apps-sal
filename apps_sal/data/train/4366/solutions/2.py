def archers_ready(archers):
    try:
        return min(archers) >= 5
    except:
        return False
