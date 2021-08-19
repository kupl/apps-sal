n = int(input())
s = set()
for a in range(n):
    name = input()
    name = name.replace('u', 'oo')
    while name.count('kh') > 0:
        name = name.replace('kh', 'h')
    s.add(name)
print(len(s))
