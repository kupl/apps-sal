t = int(input())
for _ in range(t):
    n = int(input())
    '\n\ta = [0] * n\n\n\tfor i in range(n):\n\n\t\tfor j in range(i, n, i+1):\n\n\t\t\tif (j+1) % 3 == 0:\n\t\t\t\tcontinue\n\n\t\t\ta[j] = 0 if a[j] else 1\n\n\tprint(a)\n\n\t'
    i = 2
    count = 1
    while 1:
        if i * i > n:
            break
        if i % 3 != 0:
            count += 1
        i += 1
    print(count)
