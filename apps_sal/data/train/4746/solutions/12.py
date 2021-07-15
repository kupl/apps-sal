from functools import reduce
def fisHex(name, l={'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15 }):
    return reduce( lambda acc,x: acc ^ l.get(x,0), name, 0 )

