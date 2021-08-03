t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = []
    for j in range(n):
        m = sum([arr[j % n], arr[(j + 1) % n], arr[(j + 2) % n]])
        ans.append(m)
    print(max(ans))
