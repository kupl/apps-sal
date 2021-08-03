t = int(input())

for _ in range(t):
    n = int(input())
    a = input().strip()
    prev = a[0]
    ans = -1
    for i in a:
        if prev == i:
            ans += 1
        prev = i
    print(ans)
