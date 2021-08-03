for _ in range(eval(input())):
    a, d, l, r = list(map(int, input().split()))
    al = a + (l - 2) * d
    s = 0
    for i in range(l, r + 1):
        al += d
        s += al % 9 * 1 or 9
    print(s)
