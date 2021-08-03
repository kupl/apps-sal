t = int(input())
for i in range(t):
    l = list(map(int, input().split()))
    l.sort()
    if l[0] == 0:
        s = 'NO'
    else:
        for d in range(3):
            n = l[d]**2
            k = l[d - 1]**2
            j = l[d - 2]**2
            if n == k + j:
                s = 'YES'
                break
            else:
                s = 'NO'
    print(s)
