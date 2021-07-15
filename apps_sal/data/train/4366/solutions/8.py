def archers_ready(archers):
    if not archers:
        return False
    for arrows in archers:
        if arrows < 5:
            return False
    return True
