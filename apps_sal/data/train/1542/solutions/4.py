for e in range(int(input())):
    n = int(input())
    s = input()
    l = list(map(int, input().split()))
    s = list(s)
    m = 0
    for i in range(n - 7):
        total = 0
        k = 0
        DT = 1
        for j in range(i, i + 8):
            if s[j] == '.':
                total += l[k]
            elif s[j] == 'd':
                total += (2 * l[k])
            elif s[j] == 't':
                total += (3 * l[k])
            elif s[j] == 'D':
                DT = DT * 2
                total += l[k]
            elif s[j] == 'T':
                DT = DT * 3
                total += l[k]
            k += 1

        total = total * DT
        m = max(total, m)

    print(m)
