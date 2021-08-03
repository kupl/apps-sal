from sys import stdin, stdout


T = int(stdin.readline().strip())

for _ in range(T):
    n, m = stdin.readline().strip().split(' ')
    n, m = int(n), int(m)
    mast = [[[], []] for i in range(n)]
    for hola in range(m):
        i, j, k = stdin.readline().strip().split(' ')
        i, j, k = int(i), int(j), int(k)
        i -= 1
        j -= 1
        mast[i][0].append(k)
        if j + 1 < n:
            mast[j + 1][1].append(k)

    tot = 0
    ini = 10

    for i in mast:

        for j in i[0]:
            ini *= j
        for j in i[1]:
            ini = ini // j
        tot += ini

    tot = tot // n

    stdout.write(str(tot) + "\n")
