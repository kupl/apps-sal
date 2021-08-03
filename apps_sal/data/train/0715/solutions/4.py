s = input().strip()
n = len(s)
c = 0
for i in range(n):
    c += (26 - (ord(s[i]) - 65))
print(c + n)
