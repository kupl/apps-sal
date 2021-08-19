def lordoftherings(m, n):
    if n < 9:
        return (0, 0)
    digits = len(str(n))
    mul = '9' * digits
    if int(mul) > n:
        mul = digits - 1
    else:
        mul = digits
    return (m * mul % 1000000007, m)


for _ in range(int(input())):
    (m, n) = map(int, input().split())
    (x, y) = lordoftherings(m, n)
    print(x, y)
