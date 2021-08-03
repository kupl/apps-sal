def main():
    n, l = int(input()), list(map(int, input().split()))
    if not (n & 1):
        l.append(0)
    l.append(150001)
    a, b, fails, tmp, res = 0, 150001, [], [], 0
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
    for b in fails:
        tmp.append("><"[b & 1] if b - a == 1 else "and ")
        tmp.append("l[{:n}]".format(b))
        a = b
    check = compile("".join(tmp[1:]), "<string>", "eval")
    for i in fails:
        a = l[i]
        for j in range(0, n, 2):
            l[i], l[j] = l[j], a
            if l[j - 1] > a < l[j + 1] and eval(check):
                res += 1 if j in fails else 2
            l[j] = l[i]
        for j in range(1, n, 2):
            l[i], l[j] = l[j], a
            if l[j - 1] < a > l[j + 1] and eval(check):
                res += 1 if j in fails else 2
            l[j] = l[i]
        l[i] = a
    print(res // 2)


def __starting_point():
    main()


__starting_point()
