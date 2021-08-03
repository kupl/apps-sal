t = int(input())
while t > 0:
    s = set(input())
    ans = 0
    for c in input():
        if c in s:
            ans += 1
    print(ans)
    t -= 1
