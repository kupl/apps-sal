def divisible_count(x,y,k):
    upper = y//k
    lower = (x-1)//k
    return upper - lower
