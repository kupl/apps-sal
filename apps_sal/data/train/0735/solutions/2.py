t = eval(input())
while t:
    t = ~(-t)
    n = eval(input())
    print("NO" if (n == 2 or n % 2 != 0) else "YES")
