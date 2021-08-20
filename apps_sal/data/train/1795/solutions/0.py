def nQueen(n):
    if n == 2 or n == 3:
        return []
    (r, odds, evens) = (n % 6, list(range(1, n, 2)), list(range(0, n, 2)))
    if r == 2:
        evens[:2] = evens[:2][::-1]
        evens.append(evens.pop(2))
    if r == 3:
        odds.append(odds.pop(0))
        evens.extend(evens[:2])
        del evens[:2]
    return odds + evens
