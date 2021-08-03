for t in range(int(input())):
    n = int(input())
    s = []
    a = list(map(int, input().split()))
    steps = 0
    for i in range(n):
        if (a[i] == 0):
            s = [i + 1] + s
        else:
            pos = s.index(a[i]) + 1
            steps += min(pos, i - pos)
            s = s[:pos] + [i + 1] + s[pos:]
    print(steps)
