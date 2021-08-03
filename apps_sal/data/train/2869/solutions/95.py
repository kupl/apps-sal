def distinct(seq):
    sol = []
    for num in seq:
        if num not in sol:
            sol.append(num)
    return sol
