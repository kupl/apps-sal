t = int(input())
for _ in range(t):
    (p, idx) = list(map(int, input().split()))
    length = 2 ** p
    somma = 0
    mult = 1
    while length > 1:
        length = length >> 1
        if idx >= length:
            idx -= length
            somma += mult
        mult *= 2
    print(somma)
