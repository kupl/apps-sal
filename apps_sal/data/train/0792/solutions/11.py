t = int(input())
while(t > 0):
    n, s = map(str, input().split())
    n = int(n)
    if n <= len(s):
     print("0")
    else:
     m = pow(26, n - len(s) - 1, 1000000007)
     m = m * (26 + 25 * len(s))
     print(m % 1000000007)
    t = t - 1
