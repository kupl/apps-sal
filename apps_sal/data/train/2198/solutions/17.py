n = int(input())
d = {}
for _ in range(n):
    s = input()
    while True:
        if s.find('kh') != -1:
            s = s.replace('kh', 'h')
        elif s.find('u') != -1:
            s = s.replace('u', 'oo')
        else:
            break
    d[s] = d.get(s, 0) + 1
print(len(d))
