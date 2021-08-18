t = int(input())
for i in range(t):
    n = int(input())
    if n % 2 == 0:
        print("NO")
    else:
        print("YES")
        s = ''
        s = s + '0'
        for j in range(n // 2):
            s += '1'
        for j in range(n // 2 + 1, n):
            s += '0'
        print(s)
        k = n - 1
        for j in range(n - 1):
            s1 = s[0:len(s) - 1]
            s2 = s[len(s) - 1:]
            s = s2 + s1
            print(s)
