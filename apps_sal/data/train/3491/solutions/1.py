def substring(strng):
    best = ''
    best_end = ''
    for c in strng:
        best_end += c
        while len(set(best_end + c)) > 2:
            best_end = best_end[1:]
        if len(best_end) > len(best):
            best = best_end
    return best
