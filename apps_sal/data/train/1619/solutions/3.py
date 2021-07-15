import math
def decompose(n):
    value = n-1
    remains = n**2
    cache = {value : remains}
    remains -= value**2
    
    while remains:
        value = int(math.sqrt(remains))
        if value < min(cache.keys()):
            cache[value] = remains
            remains -= value**2
        else:
            del cache[min(cache.keys())]
            if not cache: return None
            value = min(cache.keys())
            remains = cache.pop(value)
            cache[value-1] = remains
            remains -= (value-1)**2
    return sorted(cache.keys())
