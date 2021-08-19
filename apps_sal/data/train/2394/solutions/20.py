t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    left = 0
    ans = 0
    for x in s:
        if x == '(':
            left += 1
        elif left > 0:
            left -= 1
        else:
            ans += 1
    print(ans)
