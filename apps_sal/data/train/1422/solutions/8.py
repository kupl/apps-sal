t = int(input())
for nTest in range(t):
    n = int(input())
    s = input().strip()
    ns = int(s) + int(s[1:] + '0') + int('0' + s[:-1])
    ss = str(ns)
    print(ss.count('0') + len(s) - len(ss))
