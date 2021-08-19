(n, l) = map(int, input().split())
a = []
for i in range(n):
    s = input()
    a.append(s)
a.sort()
print(''.join(a))
