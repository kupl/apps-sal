def find_multiples(integer, limit):
    sol = []
    for i in range(1, (limit // integer) + 1):
        sol.append(integer * i)
    return sol
