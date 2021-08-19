# cook your dish here
t = int(input())
for i in range(t):
    n, m = list(map(int, input().split()))
    ans = n * pow(n - 1, m, 10**9 + 7) % (10**9 + 7)
    print(ans)
