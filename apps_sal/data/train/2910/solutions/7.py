def small_enough(a, limit): 
    return all(map(lambda x: x <= limit, a))
