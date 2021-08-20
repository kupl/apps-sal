fib = [1, 1]
for i in range(39):
    fib.append(fib[i] + fib[i + 1])


def mysterious_pattern(l, m):
    lines = [['o' if n % m == i else ' ' for n in fib[:l]] for i in range(m)]
    return '\n'.join((''.join(line).rstrip() for line in lines)).strip('\n')
