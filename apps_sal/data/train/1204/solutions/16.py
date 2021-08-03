for _ in range(int(input())):
    s = input()
    ss = input()
    ind = [i for i in range(len(s)) if s[i] != ss[i]]
    a = [ind[i + 1] - ind[i] - 1 for i in range(len(ind) - 1)]
    a.sort()
    ig, ire = len(ind), len(ind)
    b = [ig * ire]
    for i in a:
        ig -= 1
        ire += i
        b.append(ig * ire)
    print(min(b))
