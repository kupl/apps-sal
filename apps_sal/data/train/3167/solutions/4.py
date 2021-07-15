def twos_difference(lst): 
    matches = []
    for n in sorted(lst):
        if((n + 2) in lst):
            matches.append((n, n+2))
    return matches
