# Your new function as given to you by me, your boss.
def cut_log(p, n):
    values = [0 for _ in range(n + 1)]

    # Some array to store calculated values
    for j in range(1, n + 1):
        values[j] = p[j]
        for i in range(1, j + 1):  # Two nested loops = Θ(n^2)
            v = values[i] + values[j - i]
            if v > values[j]:
                values[j] = v
            # Magic
    return values[n]  # Good luck intern!
