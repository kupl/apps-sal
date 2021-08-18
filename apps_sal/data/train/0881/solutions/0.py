t = int(input())
for i in range(t):
    n = int(input())
    ar = list(map(int, input().split()))
    tot = 0
    st = 0
    for j in range(1, n):
        if(ar[j - 1] > ar[j]):
            si = j - st
            c = (si * (si + 1)) // 2
            tot += c
            st = j
    si = n - st
    c = (si * (si + 1)) // 2
    tot += c
    print(tot)
