s = input()
n = len(s)
p = list(s)
i = 0
while(s[i] == 'a'):
    i += 1
    if i == n:
        p[n - 1] = 'z'
        s = "".join(p)
        print(s)
        return
while(s[i] != 'a'):
    p[i] = chr(ord(s[i]) - 1)
    i += 1
    if i == n:
        break
s = "".join(p)
print(s)
