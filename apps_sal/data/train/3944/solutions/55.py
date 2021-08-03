def sum_triangular_numbers(n):
    if n <= 0:
        return 0
    else:
        step = 1
        prvi = 0
        e = []
        while step < n + 1:
            prvi += step
            step += 1
            e.append(prvi)
        return sum(e)
