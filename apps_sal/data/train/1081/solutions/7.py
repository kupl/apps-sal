n = int(input())
l = [98, 57, 31, 45, 46]
f = ''
for i in range(0, n):
    s = input().strip()
    for z in range(0, len(s)):
        k = ord(s[z]) - 65
        k = k + l[z]
        req = k % (26)
        req = req + 65
        f = f + chr(req)
    print(f)
    f = ''
