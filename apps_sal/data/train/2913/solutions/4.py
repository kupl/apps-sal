def x(n):
    m = n - 1
    return '\n'.join(
        ''.join('□■'[i + j == m or i == j] for j in range(n))
        for i in range(n)
    )
