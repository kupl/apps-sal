x = pow(10, 9) + 7
for i in range(int(input())):
    n = int(input())
    ans = pow(n, 3) + pow(n - 1, 2)
    print(ans % x)
