def base5(n):
    if n == 0:
        return
    for x in base5(n // 5):
        yield x
    yield n % 5


def seq(n):
    return int(''.join(str(2 * x) for x in base5(n)) or '0')


for i in range(eval(input())):
    k = eval(input())
    while(i < k):
        i = i + 1
    print(seq(i - 1))
