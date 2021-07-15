def nQueen(n):
    if n in [2, 3]: return []

    odds = [*range(1, n, 2)]
    evens = [*range(0, n, 2)]

    if n % 6 == 2:
        evens[:2] = evens[:2][::-1]
        evens.append(evens.pop(2))
    elif n % 6 == 3:
        odds.append(odds.pop(0))
        evens += evens[:2]
        del evens[:2]

    return odds + evens
