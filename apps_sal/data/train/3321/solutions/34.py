def evil(n):
    return "It's Evil!" if not bin(n)[2:].count("1") % 2 else "It's Odious!"
