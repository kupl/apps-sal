# cook your dish here
for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().strip().split()))
    ans = [0] * (n+1)
    nos = [1] * (n+1)
    for i in range(n-2, -1, -1):
        nos[p[i]] += nos[i+2]
        ans[i+2] += nos[i+2]
        ans[p[i]] = max(ans[p[i]], ans[i+2])
    print(ans[1] + nos[1])

