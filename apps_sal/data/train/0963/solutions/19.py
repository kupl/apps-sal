t = int(input())
for i in range(t):
    n = int(input())
    h = list(map(int, input().split()))

    def res(a):
        n = len(a)
        max1 = max(a)
        ind = 0
        ind = a.index(max1)
        if(ind == 0 or ind == n - 1):
            return 1
        else:
            return 1 + min(res(a[:ind]), res(a[ind + 1:]))
    print(res(h))
