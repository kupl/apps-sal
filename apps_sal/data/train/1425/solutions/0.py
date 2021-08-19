t = int(input())
count = []
for i in range(t):
    s = input()
    (a, b, c, n) = s.split()
    n = int(n)
    d = int(a + b * n + c, 2)
    count.append(0)
    while d > 0:
        d = (d & d + 1) - 1
        count[i] += 1
for i in range(t):
    print(count[i])
