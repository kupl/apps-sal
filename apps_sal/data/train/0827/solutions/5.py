try:
    for _ in range(int(input())):
        (n, k) = map(int, input().split())
        string = input()
        cnta = cntb = ab = 0
        for i in string:
            if i == 'a':
                cnta += 1
            elif i == 'b':
                cntb += 1
                ab += cnta
        final = ab * k
        final += k * (k - 1) * cnta * cntb // 2
        print(final)
except:
    pass
