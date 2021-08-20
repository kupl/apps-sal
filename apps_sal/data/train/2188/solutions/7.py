n = int(input())
a = []
wk1 = '0' * 18
rules = str.maketrans('0123456789', '0101010101')


def trans(x):
    return str.translate(x, rules)


d = {}
for _ in range(n):
    (x, y) = input().split()
    y = int(trans(y), 2)
    if x == '+':
        d[y] = d.get(y, 0) + 1
    elif x == '-':
        d[y] -= 1
    elif x == '?':
        print(d.get(y, 0))
