def evil(n):
    evil = bin(n)[2:].count('1') % 2 == 0
    return "It's Evil!" if evil else "It's Odious!"
