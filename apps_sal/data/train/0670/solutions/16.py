from fractions import gcd

for t in range(eval(input())):
    n = eval(input())
    ans = 0
    for x in map(int, input().split()):
        ans = gcd(ans, x)
    print(ans * n)
