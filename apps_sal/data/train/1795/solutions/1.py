def nQueen(n):
    if n == 1:
        return [0]
    if n <= 3:
        return []

    evens = [i for i in range(2, n + 1, 2)]
    odds = [i for i in range(1, n + 1, 2)]

    if n % 6 == 3:
        evens.remove(2)
        evens.append(2)
        odds.remove(1)
        odds.remove(3)
        odds.append(1)
        odds.append(3)
    elif n % 6 == 2:
        odds[0], odds[1] = 3, 1
        odds.remove(5)
        odds.append(5)

    return [a - 1 for a in evens + odds]
