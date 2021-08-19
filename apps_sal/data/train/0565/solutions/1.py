from sys import stdin, stdout
t = int(stdin.readline())
while t:
    (n, q) = list(map(int, stdin.readline().rstrip().split()))
    arr = list(map(int, stdin.readline().rstrip().split()))
    d = {}
    d1 = {}
    a = arr.copy()
    a.sort()
    for i in range(n):
        d1[a[i]] = i
        d[arr[i]] = i
    while q:
        v = int(stdin.readline().rstrip())
        index = d[v]
        smaller = d1[v]
        bigger = n - smaller - 1
        (low, high) = (0, n - 1)
        (c1, c2) = (0, 0)
        while high >= low:
            mid = (high + low) // 2
            if mid == index:
                break
            elif index > mid:
                if arr[mid] > v:
                    c1 += 1
                else:
                    smaller -= 1
                low = mid + 1
            else:
                if v > arr[mid]:
                    c2 += 1
                else:
                    bigger -= 1
                high = mid - 1
        if c2 > c1:
            if bigger >= c2 - c1:
                print(c2)
            else:
                print(-1)
        elif c1 > c2:
            if smaller >= c1 - c2:
                print(c1)
            else:
                print(-1)
        else:
            print(c1)
        q -= 1
    t -= 1
