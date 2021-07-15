for _ in range(int(input())):
    n = int(input())
    l = 1
    i = 1
    while l <= n:
        s = ''
        for j in range(l):
            s = str(i) + s
            i += 1
        print(s)
        l += 1
