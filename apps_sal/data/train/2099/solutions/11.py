from itertools import permutations


def main():
    n, k = map(int, input().strip().split())
    a = b = k // 2 + 1
    delta = (k & 1) * 2 - 1
    res = []
    for _ in range(k // 2):
        res.append(a)
        a -= delta
        b += delta
        res.append(b)
    if k & 1:
        res.append(a)
    for a in range(k + 1, n + 1):
        res.append(a)
    print(*res)


main()
