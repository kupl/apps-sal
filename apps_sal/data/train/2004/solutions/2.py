s = input()
if s.count('0') == 0:
    print(s[1:])
else:
    i = s.index('0')
    print(s[:i] + s[i + 1:])
