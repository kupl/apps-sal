# cook your dish here
for i in range(int(input())):
    n, m = list(map(int, input().split()))
    if(n == 1):
        print(0)
        continue
    if(n == 2):
        print(m)
        continue
    ans = (n - 1) + 2 * (m - 1)
    print(ans)
