n = int(input())
names = {}
for i in range(n):
    s = input()
    while s.find('kh') != -1:
        s = s.replace('kh', 'h')
    while s.find('u') != -1:
        s = s.replace('u', 'oo')
    names[s] = 1
print(len(names))
