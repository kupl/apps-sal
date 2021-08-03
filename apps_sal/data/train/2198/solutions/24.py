n = int(input())
e = set()
for i in range(n):
    s = input()
    while 1:
        s1 = s
        s = s.replace('u', 'oo').replace('kh', 'h')
        if s == s1:
            break
    e.add(s)

print(len(e))
