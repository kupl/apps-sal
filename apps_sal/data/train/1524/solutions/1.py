test = int(input())
for i in range(1, test + 1):
    a = input().split(" ")
    n = int(a[0])
    k = int(a[1])
    ans = pow(k - 1, n - 1, 1000000007)
    ans = (ans * k) % 1000000007
    print(ans)
