for t in range(int(input())):
    n = int(input())
    l = [0] * 8
    for i in range(n):
        p, s = list(map(int, input().split()))
        if p <= 8 and l[p - 1] < s:
            l[p - 1] = s
    print(sum(l))
