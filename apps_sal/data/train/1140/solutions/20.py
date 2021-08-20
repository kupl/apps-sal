def calc(i, p):
    if p == 1:
        return [0, 1][i]
    if i >= 2 ** (p - 1):
        t = calc(i - 2 ** (p - 1), p)
        return t + 1
    else:
        t = calc(i, p - 1)
        return 2 * t


for t in range(int(input())):
    [p, i] = [int(i) for i in input().split()]
    print(calc(i, p))
