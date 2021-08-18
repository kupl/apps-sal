t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    for k in range(n * m):
        s = ''
        t = ''
        for i in range(n * m):
            s += '0'
        i = 0
        while(i < len(s)):
            s = s[:i] + '1' + s[i + 1:]
            i += k + 1
        i = 0
        for i in range(n):
            while(i < len(s)):
                t += s[i]
                i += n
        i = 0
        while(i < len(t)):
            t = t[:i] + '1' + t[i + 1:]
            i += k + 1
        print(t.count('1'), ' ', end='')
