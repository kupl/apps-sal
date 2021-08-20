t = int(input())
rules = str.maketrans('0123456789', '0101010101')


def trans(x):
    return str.translate(x, rules)


(cnt, res) = ({}, [])
for _ in range(t):
    (op, n) = input().split()
    n = int(trans(n), 2)
    if op == '+':
        cnt[n] = cnt.get(n, 0) + 1
    elif op == '-':
        cnt[n] -= 1
    else:
        res.append(str(cnt.get(n, 0)))
print('\n'.join(res))
