from fileinput import *

for line in input():
    if lineno() == 1:
        [n, k] = list(map(int, line.split()))


a = [i+1 for i in range(n)]

b = a[:k+1]
bend = a[k+1:]
lb = len(b)

if lb % 2 == 1:
    middle = lb // 2 + 1
else:
    middle = lb // 2

b[::2], b[1::2] = b[:middle], b[:middle-1:-1]

answer = b + bend

s = ''.join([str(x) + ' ' for x in answer])
print(s.strip())

