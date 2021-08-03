t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mp = {}
    for i in a:
        mp[i] = 0
    ans = []
    for i in a:
        mp[i] += 1
        if mp[i] == 1:
            ans.append(i)
    print(*ans, sep=" ")
