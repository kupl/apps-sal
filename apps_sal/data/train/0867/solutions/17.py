x = []
for t in range(int(input())):
    (s, w1, w2, w3) = list(map(int, input().strip().split()))
    z = w1 + w2 + w3
    c = 0
    while z > 0:
        z = z - s
        c = c + 1
    x.append(c)
for i in x:
    print(i)
