pr = [2]
sv = [0] * 203
for i in range(3, 202, 2):
    if sv[i] == 0:
        pr.append(i)
        for j in range(2 * i, 203, i):
            sv[j] = 1
sp = [0] * (5 * 10 ** 4)
for i in range(len(pr)):
    for j in range(i + 1, len(pr)):
        sp[pr[i] * pr[j]] = 1
for _ in range(int(input())):
    n = int(input())
    an = 'NO'
    for i in range(1, n):
        if sp[i] and sp[n - i]:
            an = 'YES'
            break
    print(an)
