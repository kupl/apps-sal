t = eval(input())
for test in range(t):
    s = input()
    s = s[::-1]
    ans = ''
    i = 0
    while i < len(s) and s[i] == '0':
        i = i + 1
    while i < len(s):
        ans = ans + s[i]
        i = i + 1
    print(ans)
