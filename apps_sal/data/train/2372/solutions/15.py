def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    s = input()
    return list(s[:len(s)])


def invr():
    return list(map(int, input().split()))


n = inp()
for i in range(n):
    val = inp()
    cnt = 1
    prev = 10 ** 10
    while True:
        if (val + cnt - 1) // cnt + cnt - 1 > prev:
            print(prev - 1)
            break
        else:
            prev = (val + cnt - 1) // cnt + cnt - 1
            cnt += 1
