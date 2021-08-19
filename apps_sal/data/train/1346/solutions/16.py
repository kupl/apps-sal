m = 10 ** 9 + 7
t = int(input())
for i in range(t):
    (N, W) = map(int, input().split())
    if W >= 0 and W <= 8:
        r = 9 - W
        print(pow(10, N - 2, m) * (r % m) % m)
    elif W > 8:
        print(0)
    elif W < 0 and W >= -9:
        s = 10 - abs(W)
        print(pow(10, N - 2, m) * (s % m) % m)
    else:
        print(0)
