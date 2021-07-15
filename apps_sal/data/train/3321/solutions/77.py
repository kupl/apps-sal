def evil(n):
    return "It's {}!".format(["Evil", "Odious"][bin(n)[2:].count("1")%2])
