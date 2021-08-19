(n, l) = map(int, input().split())
s = list((input() for i in range(n)))
s.sort()
a = ''
for i in range(n):
    a = a + s[i]
print(a)
