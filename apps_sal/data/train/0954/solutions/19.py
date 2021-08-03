
t = int(input())
while t > 0:
    sum = 0
    s = []
    n = int(input())
    for i in range(n):
        s.append((i + 1))
    for i in range(n - 1, 0, -1):
        s.append((i))
    for i in range(len(s)):
        sum = sum + s[i]**3
    print(sum)

    t = t - 1
