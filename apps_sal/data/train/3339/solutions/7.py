def mystery(n):

    if n <= 0:
        return []

    factors = [i for i in range(1, n + 1) if n % i == 0]

    valid = [j for j in factors if j % 2 == 1]

    return valid
