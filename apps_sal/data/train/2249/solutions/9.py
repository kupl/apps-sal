def testcase():
    (x1, y1, x2, y2) = map(int, input().split())
    x = abs(x1 - x2)
    y = abs(y1 - y2)
    ans = x + y
    if x > 0 and y > 0:
        ans += 2
    print(ans)
    return


t = int(input())
for _ in range(t):
    testcase()
