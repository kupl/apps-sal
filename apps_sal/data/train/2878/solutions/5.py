def shortest_to_char(alist, target):
    # find all locations of target character
    loc = [i for i, x in enumerate(alist) if x == target]
    if not loc: return []

    # for every character in the alist, find the minimum distance
    # to one or more target characters
    shortest = [min(abs(i - l ) for l in loc) for i in range(len(alist))] 
    return shortest

