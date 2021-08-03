n = int(input())
x = [int(i) for i in input().split()]
m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    t = b - 1
    t1 = x[a] - b
    if a - 1 >= 0:
        x[a - 1] += t
    if a + 1 < n:
        x[a + 1] += t1
    x[a] = 0
for i in x:
    print(i)
