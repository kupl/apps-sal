n = int(input())
s = 0
c = 10 ** 10
for i in range(n):
    (a, b) = map(int, input().split())
    s = s + a
    if a > b:
        if b < c:
            c = b
if c == 10 ** 10:
    print(0)
else:
    print(s - c)
