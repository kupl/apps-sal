t = int(input())
while t > 0:
    ans = []
    n, m = list(map(int, input().split()))
    temp = []
    for k in range(0, n * m):
        myset1 = set()
        myset2 = set()
        if k == 0:
            ans.append(n * m)
        elif k == n * m - 1:
            ans.append(1)
        else:
            for j in range(1, m + 1):
                i = j
                while i <= n * m:
                    temp.append(i)
                    i += m
            i = 1
            while i <= n * m:
                myset1.add(i)
                i = i + k + 1
            i = 0
            while i <= n * m - 1:
                myset2.add(temp[i])
                i = i + k + 1
            current = list(myset1.union(myset2))
            ans.append(len(current))
    print(*ans)
    t -= 1
