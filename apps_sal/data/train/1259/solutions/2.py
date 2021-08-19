t = int(input())
for i in range(t):
    (l, r) = list(map(int, input().split()))
    ans = 0
    for i in range(l, r + 1):
        ck = str(i)[-1]
        if ck == '2' or ck == '3' or ck == '9':
            ans += 1
    print(ans)
