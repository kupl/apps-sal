def evil(n):
    return "It's %s!" % ["Evil","Odious"][bin(n).count("1")%2]
