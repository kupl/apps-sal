
x = int(input())
while(x > 0):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    maxN = 0
    for i in range(n - 1):
        b = []
        b.append(a[i])
        t = 1
        while(i + t < n):
            b.append(a[i + t])
            b.sort(reverse=True)
            if(b[0] + b[1] <= k):
                t += 1
            else:
                break
        if(maxN < t):
            maxN = t
    print(maxN)
    x -= 1
