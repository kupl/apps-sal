import sys
msg = sys.stdin.readlines()

l = []

for i in msg:
    l.append(list(map(int, i.split())))


def sm(x): return int(x * (x + 1) * 1)


def timew(n, k):
    if n == 0:
        time = sm(k - 1)
    else:
        if k == 1:
            time = (n - 1) * (n) + n
        else:
            if k % 2 == 1:
                pre_rounds = (k - 1) // 2
                time = sm(n + pre_rounds - 1) + n + 2 * (pre_rounds)
            else:
                pre_rounds = (k) // 2
                time = sm(n + pre_rounds - 1) + n
    return time % 1000000007


for i in l[1:]:
    [n, k] = i
    print(timew(n, k))
