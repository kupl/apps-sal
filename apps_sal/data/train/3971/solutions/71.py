def tidyNumber(n):
    return sorted(map(int,str(n))) == list(map(int,str(n)))
