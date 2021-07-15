t = int(input())
for i in range(t):
    (a, b, c, d, e, f) = list(map(int, input().split()))
    x = -max({a, c, e}) + a + c + e
    y = -max({b, d, f}) + b + d + f
    print((max(abs(x), abs(y)) + (x == y and x and x != 1)))

