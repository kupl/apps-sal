3
(s, t) = input().split()
print(s, t)
n = int(input())
for i in range(n):
    (w, y) = input().split()
    if s == w:
        s = y
    else:
        t = y
    print(s, t)
