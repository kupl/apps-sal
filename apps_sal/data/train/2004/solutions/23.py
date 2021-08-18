
from sys import stdin, stdout
input = stdin.readline

a = input()[:-1]

dl = -1
for i in range(len(a)):
    if a[i] == "0":
        dl = i
        break

a = list(a)
a.pop(i)
stdout.write("".join(a))
