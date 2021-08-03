t = int(input())
while(t > 0):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    l = []
    mx = -1000000000
    start = 0
    for end in range(n):
        l.append(a[end])
        while(len(set(l)) >= k):
            l.pop(0)
            start += 1
        if(end - start + 1 > mx):
            mx = end - start + 1
    print(mx)
    t = t - 1
