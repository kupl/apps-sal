def list_squared(m, n):
    out = []
    for i in range(m, n + 1):
        # Finding all divisors below the square root of i
        possibles = set([x for x in range(1, int(i**0.5) + 1) if i % x == 0])
        # And adding their counterpart
        possibles.update([i / x for x in possibles])
        # Doubles in the possibles are solved due to the set
        val = sum(x**2 for x in possibles)
        # Checking for exact square
        if (int(val**0.5))**2 == val:
            out.append([i, val])
    return out
