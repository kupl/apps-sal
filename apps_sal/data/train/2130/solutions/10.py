from math import factorial
n, ans, s = int(input()), 1, 0
for i in range(n):
    a = int(input())
    ans = (ans * factorial(s + a - 1) // factorial(s) // factorial(a - 1)) % 1000000007
    s += a
print(ans)


# copied...
