import sys
"\nsys.stdin = open('input.txt', 'r') \nsys.stdout = open('output.txt', 'w')\n"
n = int(input())
names = []
for _ in range(n):
    names.append(input())
other = []
for name in names:
    while 'u' in name:
        name = name.replace('u', 'oo')
    while 'kh' in name:
        name = name.replace('kh', 'h')
    other.append(name)
print(len(set(other)))
