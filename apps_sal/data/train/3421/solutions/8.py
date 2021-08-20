def mysterious_pattern(m, n):
    fib = [1, 1]
    for i in range(m - 2):
        fib.append(fib[-1] + fib[-2])
    ret = [['o' if fib[x] % n == y else ' ' for x in range(m)] for y in range(n)]
    return '\n'.join((''.join(row).rstrip() for row in ret)).strip('\n')
