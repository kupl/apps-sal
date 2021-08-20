t = int(input())
for i in range(t):
    (a, b) = input().split()
    (a, b) = (int(a), int(b))
    if a == 0:
        b = b * 2
    ans = pow(a, 2) + int(b / 2) * 2 * a + pow(int(b / 2) - 1, 2) + int(b / 2) - 1
    if b % 2 != 0:
        ans = ans + b - 1
    print(ans % 1000000007)
