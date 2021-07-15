def main():
    n, l = int(input()), list(map(int, input().split()))
    if not (n & 1):
        l.append(0)
    l.append(150001)
    a, b, fails, res = 0, 150001, [], 0
    for i, c in enumerate(l, -1):
        if i & 1:
            if a >= b or b <= c:
                if len(fails) > 5:
                    print(0)
                    return
                fails.append(i)
        else:
            if a <= b or b >= c:
                if len(fails) > 5:
                    print(0)
                    return
                fails.append(i)
        a, b = b, c
    check = compile("and".join(
        "(l[{:n}]{:s}l[{:n}]{:s}l[{:n}])".format(i - 1, "><"[i & 1], i, "<>"[i & 1], i + 1) for i in fails),
                   "<string>", "eval")
    for i in fails:
        a = l[i]
        for j in range(n):
            l[i], l[j] = l[j], a
            if eval(check) and ((l[j - 1] < l[j] > l[j + 1]) if j & 1 else (l[j - 1] > l[j] < l[j + 1])):
                res += 1 if j in fails else 2
            l[j] = l[i]
        l[i] = a
    print(res // 2)


def __starting_point():
    main()



# Made By Mostafa_Khaled

__starting_point()
