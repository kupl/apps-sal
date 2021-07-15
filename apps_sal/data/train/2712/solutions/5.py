def loneliest(number): 
    numbers = [int(c) for c in str(number)]
    loneliness = [(n, sum(numbers[max(i-n, 0):i]) + sum(numbers[i+1:i+1+n])) for i, n in enumerate(numbers)]
    onesLoneliness = [p[1] for p in loneliness if p[0] == 1]
    if (not onesLoneliness) : return False
    otherLoneliness = [p[1] for p in loneliness if not p[0] == 1]
    if (not otherLoneliness): return True
    return min(otherLoneliness) >= min(onesLoneliness)
