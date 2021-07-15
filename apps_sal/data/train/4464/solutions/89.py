def feast(beast, dish):
    start = beast.startswith(dish[0])
    finish = beast.endswith(dish[-1:])
    
    if start and finish:
        return True
    return False
