def the_biggest_search_keys(*keys):
    m = max(map(len, keys)) if keys else None
    return str( sorted( filter(lambda x: len(x) == m, keys) ) )[1:-1] if keys else "''"
