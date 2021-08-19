# cook your dish here
t = int(input())
for i in range(t):
    x = int(input())
    sol = (pow(2, x, 8589934592) - 1) % 8589934592
    ans = "Case " + str((i + 1)) + ": " + str(sol)
    print(ans)
