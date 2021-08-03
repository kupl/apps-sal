t = int(input())
while(t):
    n = int(input())
    ans = n * (n + 1) * (2 * n + 1)
    ans = ans / 6
    print(int(ans))
    t = t - 1
