def evil(anum):
    thecount = bin(anum).count('1')
    if thecount % 2 == 0:
        return 'It\'s Evil!'
    elif thecount % 2 != 0:
        return 'It\'s Odious!'
