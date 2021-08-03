for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    if 'a' not in s:
        print(0)
        continue
    cnta = 0
    cntb = 0
    c = 0
    for i in s:
        if i == 'a':
            cnta += 1
        elif i == 'b':
            cntb += 1
            c += cnta
    ans = c * k
    ans = ans + k * (k - 1) // 2 * cnta * cntb
    print(ans)
