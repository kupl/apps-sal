for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    s = 0
    l.sort(reverse=True)
    for i in range(0, n, 2):
        s = s + l[i]
    print(s)
