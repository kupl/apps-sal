def base5(n):
    if n == 0:
        return
    for x in base5(n // 5):
        yield x
    yield n % 5


def seq(n):
    return int(''.join(str(2 * x) for x in base5(n)) or '0')


t = eval(input())
for i in range(t):
    k = eval(input())
    print(seq(k - 1))
