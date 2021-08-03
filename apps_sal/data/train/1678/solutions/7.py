n, m = map(int, input().split())

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

a = l1.index(min(l1))
b = l2.index(max(l2))

for i in range(m):
    print(a, i)

for i in range(n):
    if a != i:
        print(i, b)
