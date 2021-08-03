def whoseMove(l, w): return l if w else "".join([chr(x ^ y) for x, y in zip([21, 4, 8, 23, 14], l.encode())])
