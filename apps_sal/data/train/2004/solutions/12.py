s = input()
f = True
try:
    idx = s.index('0')
    print(s[:idx] + s[idx + 1:])
    f = False
except:
    pass
if f:
    print(s[1:])
