CA = []
IA = []
for i__i in range(eval(input())):
    n = eval(input())
    for __ in range(n):
        zz, ex = list(map(int, input().split()))
        if ex == 0:
            continue
        if (ex > 1):
            CA.append(str(zz * ex) + "x^" + str(ex - 1))
        if (ex == 1):
            IA.append((zz * ex))
    k = sum(IA)
    if k > 0:
        CA.append(str(k))
    str1 = ' + '.join(str(e) for e in CA)
    if len(str1) >= 1:
        print(str1)
    else:
        print("0")
    CA[:] = []
    IA[:] = []
