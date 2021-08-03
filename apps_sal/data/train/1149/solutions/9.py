from sys import stdin, stdout
mod = 10**7 + 9
for _ in range(int(stdin.readline())):
    s = input().strip()
    n = len(s)
    m = 1
    for i in range(n // 2):
        # print(i,n-i-1)
        if s[i] == s[n - i - 1] and s[i] == '?':
            m = (m * 26) % mod
        elif s[i] != s[n - i - 1] and (s[i] == '?' or s[n - i - 1] == '?'):
            pass
        elif s[i] == s[n - i - 1]:
            pass
        else:
            print(0)
            break
    else:
        if n % 2 == 1 and s[n // 2] == '?':
            m = (m * 26) % mod
        print(m)
