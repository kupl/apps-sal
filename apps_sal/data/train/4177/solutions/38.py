def men_from_boys(arr):
    E, U = set(), set()
    for n in arr:
        U.add(n) if n % 2 else E.add(n)
    return sorted(E) + sorted(U, reverse=True)
