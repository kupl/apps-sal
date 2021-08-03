t = int(input())

for _ in range(t):
    n, k = (int(i) for i in input().split())
    cust = [[int(i) for i in input().split()] for _ in range(n)]
    cust.sort(key=lambda x: x[1])

    compartments = {}
    ans = 0
    for x in cust:
        s, f, c = x
        if c in compartments:
            if compartments[c] <= s:
                compartments[c] = f
                ans += 1
        else:
            compartments[c] = f
            ans += 1

    print(ans)
