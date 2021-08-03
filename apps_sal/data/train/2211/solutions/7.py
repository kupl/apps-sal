a = int(input())
for i in range(a):
    n, d = map(int, input().split())
    m = list(map(int, input().split()))
    ui = 1e10
    for l in m:
        ans = 0
        if d % l != 0:
            ans += 1
        ans += d // l
        if d // l == 0 and d % l != 0:
            ans += 1
        ui = min(ui, ans)
    print(int(ui))
