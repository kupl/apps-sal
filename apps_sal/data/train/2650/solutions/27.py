(n, l) = map(int, input().split())
a = []
for i in range(n):
    a.append(input())
a.sort()
print(''.join(a))
