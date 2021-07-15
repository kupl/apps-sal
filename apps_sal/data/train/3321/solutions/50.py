def evil(n):
    return 'It\'s Odious!' if sum(map(int,list(bin(n)[2:])))%2 else 'It\'s Evil!'
