def mysterious_pattern(m, n):
    exp = [[(' ', 'o')[j == e % n] for e in fib(m)] for j in range(n)]
    return '\n'.join((''.join(e).rstrip() for e in exp)).strip('\n')


def fib(n):
    ret = [1, 1]
    for i in range(n):
        ret.append(ret[-1] + ret[-2])
    return ret[:-2]
