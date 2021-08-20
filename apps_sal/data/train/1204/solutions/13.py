for i in range(int(input())):
    s = input()
    r = input()
    (k, l, f) = (0, 0, 0)
    ff = []
    farhan = False
    for i in range(len(s)):
        if s[i] == r[i]:
            if farhan:
                f += 1
        else:
            if not farhan:
                k += 1
            farhan = True
            l += 1
            if f > 0:
                k += 1
                ff.append(f)
                f = 0
    ff.sort()
    sol = k * l
    for i in range(len(ff)):
        l += ff[i]
        k -= 1
        sol = min(sol, k * l)
    print(sol)
