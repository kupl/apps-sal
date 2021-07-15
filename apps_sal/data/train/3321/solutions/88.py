def evil(n):
    b=bin(n)
    l=list(b)
    return "It's Evil!" if l[2:].count("1")%2==0 else "It's Odious!"
