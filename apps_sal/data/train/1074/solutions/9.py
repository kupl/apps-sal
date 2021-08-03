for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    t = [0] * (10001)
    for i in l:
        t[i] += 1
    s = 0
    for j in t:
        s += j // 2
    print(s // 2)
