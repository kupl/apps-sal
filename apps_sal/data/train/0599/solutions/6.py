from sys import maxsize, stdout, stdin
mod = int(1000000000.0 + 7)


def I():
    return int(stdin.readline())


def lint():
    return [int(x) for x in stdin.readline().split()]


def S():
    return input().strip()


def grid(r, c):
    return [lint() for i in range(r)]


for _ in range(I()):
    n = I()
    ls = lint()
    cnt = 0
    arr = [0] * n
    m = max(ls)
    idx = ls.index(m)
    ideal = n // 2
    shift = ideal - idx
    for i in range(n):
        arr[i] = ls[(i - shift) % n]
    if m in arr[:n // 2]:
        print(0)
    else:
        for j in range(n - 1, n // 2 - 1, -1):
            if arr[j] != m:
                cnt += 1
            else:
                break
        print(cnt + 1)
