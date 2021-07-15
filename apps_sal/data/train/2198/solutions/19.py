import re

t = int(input())
dd = {}
for i in range(0, t):
    s = input()
    s = re.sub(r'[k]+h', 'h', s.rstrip())
    s = re.sub(r'u', 'oo', s.rstrip())
    dd[s] = 1

print(len(dd))

