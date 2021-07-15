import re
n = int(input())
b = []
for i in range(n):
    a = re.sub("[^\s\w]","",input()).split()
    b.append(' '.join(a[::-1]))

for i in b[::-1]:
    print(i)
