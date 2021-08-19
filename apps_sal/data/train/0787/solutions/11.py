# cook your dish here
# from itertools import groupby
t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    i = n - 1
    ones = s.count('1')
    c = 0
    ans = 0
    while i >= 0:
        if s[i] == '0':
            c += 1
            i -= 1
        else:
            if c:
                ans += ones * (c + 1)
                c = 0
            while i >= 0 and s[i] == '1':
                ones -= 1
                i -= 1
    print(ans)
