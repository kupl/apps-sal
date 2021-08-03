for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s = 0
    s1 = 0
    s2 = 0
    for i in range(len(a)):
        s1 += a[i]
        s2 += b[i]
        if s1 == s2 and a[i] == b[i]:
            s += a[i]
    print(s)
