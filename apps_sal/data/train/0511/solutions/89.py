N = int(input())
a = [int(s) for s in input().split()]
b = a[0]
c = []
for i in range(1, N):
    b = b ^ a[i]
for i in range(N):
    c.append(str(b ^ a[i]))
d = ' '.join(c)
print(d)
