t = int(input())
for ts in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    k = 0
    c = 0
    for j in range(n):
        if a[j] == b[k]:
            k += 1
            if k == m:
                c = 1
                print('Yes')
                break
    if c == 0:
        print('No')
