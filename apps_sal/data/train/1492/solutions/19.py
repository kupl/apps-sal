for x in range(0, int(input())):
    k = int(input())
    (ctra, ctrb) = ([None] * k, [None] * k)
    for y in range(0, k):
        s = input()
        (ctra[y], ctrb[y]) = (s.count('a'), s.count('b'))
    print(min(min(ctra), min(ctrb)))
