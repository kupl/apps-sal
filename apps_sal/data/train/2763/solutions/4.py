def sol_equa(n):
    solutions, i = [], 1
    while i * i <= n:
        if n % i == 0:
            j = n // i
            if (i + j) % 2 == 0:
                x = (i + j) // 2
                v, V = i - x, j - x
                if v % 2 == 0 and v == V * -1:
                    y = abs(v // 2)
                    solutions.append([x, y])
        i += 1
    return solutions
