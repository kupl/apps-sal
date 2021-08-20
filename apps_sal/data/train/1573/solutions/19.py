t = int(input())
for i in range(0, t):
    n = int(input())
    if n % 2 == 0:
        print('NO')
    else:
        print('YES')
        s = '0'
        for j in range(0, n // 2):
            s += '1'
        for j in range(0, n - (n // 2 + 1)):
            s += '0'
        for j in range(0, n):
            print(s)
            c = s[n - 1]
            s = s[0:n - 1]
            s = c + s
