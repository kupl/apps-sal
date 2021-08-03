def pattern(n):
    l, s = 2 * n - 1, ''.join(str(x % 10) for x in range(1, n + 1))
    lst = [(s[:-i or n] + s[:-i - 1][::-1]).center(l) for i in range(n)]
    return '\n'.join(lst[1:][::-1] + lst)
