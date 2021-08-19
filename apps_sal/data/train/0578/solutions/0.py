# cook your dish here
for i in range(int(input())):
    n, b = map(int, input().split())
    ans = round(n / (2 * b)) * (n - b * round((n / (2 * b))))
    print(ans)
