q = int(input())
for i in range(q):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    wynik = 23472983749823739
    for i in range(1, n):
        wynik = min(wynik, l[i] - l[i - 1])
    print(wynik)
