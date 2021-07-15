def animals(heads, legs):
    if legs % 2 != 0:
        return "No solutions"
    elif legs == 0 and heads == 0:
        return (0,0)
    elif heads <= 0:
        return "No solutions"
    elif legs <= 0:
        return "No solutions"
    elif heads > 1000:
        return "No solutions"
    elif legs > 1000:
        return "No solutions"
    else:
        cows = (legs/2) - heads
        chickens = heads - cows
        if cows < 0:
            return "No solutions"
        elif chickens < 0:
            return "No solutions"
    return (chickens,cows)
