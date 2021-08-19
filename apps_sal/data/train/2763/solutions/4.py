def sol_equa(n):
    # x^2 - 4y^2 = n -> return [x, y]
    # Factor to n = (x+2y)(x-2y)
    solutions, i = [], 1
    while i * i <= n:
        if n % i == 0:  # Factor found: (j=n//i: so: i*j = n)
            j = n // i
            if (i + j) % 2 == 0:  # (x + 2y)+(x - 2y)    = (2x)
                # Fits requirements for x!!!
                x = (i + j) // 2      # (i      + j )    / 2 =  x
                v, V = i - x, j - x   # (i  - x = 2y) and (j - x = -2y)
                if v % 2 == 0 and v == V * -1:
                    # Fits requirements for y!!!
                    y = abs(v // 2)
                    solutions.append([x, y])
        i += 1
    return solutions
