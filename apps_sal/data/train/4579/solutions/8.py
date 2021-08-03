def pattern(n):
    if n < 1:
        return ''
    if n == 1:
        return '1'
    res = []
    for i in range(1, n + 1):
        res.append(''.join([str(i % 10)] * i + [str(s % 10) for s in range(i + 1, n + 1)])[::-1])
    return '\n'.join(res[::-1])
