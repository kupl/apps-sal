t = int(input())
for i in range(t):
    n = int(input())
    s = 0
    for j in range(1, int(n**0.5) + 1):
        if (j) % 3 == 0:
            continue

        else:
            s += 1
    print(s)
