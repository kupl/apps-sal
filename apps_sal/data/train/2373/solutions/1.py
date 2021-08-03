from sys import stdin
input = stdin.readline
t = int(input())
for iwuehufiew in range(t):
    n, k = list(map(int, input().split()))
    l = list(map(int, input().split()))
    odc = [[1 + min(l[i], l[n - 1 - i]), k + max(l[i], l[n - 1 - i])] for i in range(n // 2)]
    cyk = [0] * (2 * k + 2)
    for o in odc:
        cyk[o[0]] += 1
        cyk[o[1] + 1] -= 1
    cov = [0] * (2 * k + 2)
    cov[0] = cyk[0]
    for i in range(1, 2 * k + 2):
        cov[i] = cov[i - 1] + cyk[i]
    ilosc = [0] * (2 * k + 1)
    for i in range(n // 2):
        ilosc[l[i] + l[n - 1 - i]] += 1
    wyn = 759237598237985732489
    for i in range(2 * k + 1):
        a = cov[i] + (n // 2 - cov[i]) * 2 - ilosc[i]
        wyn = min(wyn, a)
    print(wyn)
