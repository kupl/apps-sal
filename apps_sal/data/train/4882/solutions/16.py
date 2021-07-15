from math import ceil

# And others, take your pick
def round_to_next5(n):
    return 5*ceil(n/5)
    return n + 5 - (n%5 or 5)
    return (n+4)//5*5
