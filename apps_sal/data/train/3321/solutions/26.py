def evil(n):
    c = 0
    while(n):
        c += n & 1
        n >>= 1

    if c & 1:
        return("It's Odious!")
    else:
        return("It's Evil!")
