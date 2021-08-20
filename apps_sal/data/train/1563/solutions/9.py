for tst in range(int(input())):
    (m, n) = input().split()
    m = m[::-1]
    n = n[::-1]
    m = int(m)
    n = int(n)
    x = m + n
    x = str(x)
    x = x[::-1]
    x = int(x)
    print(x)
