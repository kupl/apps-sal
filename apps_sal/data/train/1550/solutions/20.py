def xnor(a, b):
    if a == 0:
        return 1 ^ b
    p = a
    a = a | (a >> 1)
    a = a | (a >> 2)
    a = a | (a >> 4)
    a = a | (a >> 8)
    a = a | (a >> 16)
    a = a | (a >> 32)
    a = a | (a >> 64)
    return (a ^ p) ^ b


def solve():
    a, b, n = list(map(int, input().split()))
    n -= 1
    index = n % 3
    if index == 0:
        print(a)
    elif index == 1:
        print(b)
    else:
        x = a ^ b
        e = xnor(max(a, b), min(a, b))
        print(max(x, e))


for _ in range(int(input())):
    solve()
