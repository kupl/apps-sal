for _ in range(int(input())):
    m, n = map(int, input().split())
    val = '9'
    c = 0
    while int(val) <= n:
        c += 1
        val += '9'
    if m * c != 0:
        print(m * c, m)
    else:
        print(0, 0)
