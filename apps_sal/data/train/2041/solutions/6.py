def main():
    (n, l) = (int(input()), list(map(int, input().split())))
    if not n & 1:
        l.append(0)
    l.append(150001)
    (a, i, j, fails) = (l[0], 0, 1, set())
    try:
        while True:
            b = l[j]
            if a >= b:
                fails.add(i)
                fails.add(j)
                if len(fails) > 6:
                    break
            i += 2
            a = l[i]
            if a >= b:
                fails.add(i)
                fails.add(j)
                if len(fails) > 6:
                    break
            j += 2
        print(0)
        return
    except IndexError:
        (tmp, res) = ([], 0)
    for b in sorted(fails):
        tmp.append('><'[b & 1] if b - a == 1 else 'and ')
        tmp.append('l[{:n}]'.format(b))
        a = b
    check = compile(''.join(tmp[1:]), '<string>', 'eval')
    for i in fails:
        a = l[i]
        for j in fails:
            (l[i], l[j]) = (l[j], a)
            if eval(check):
                res -= 1
            l[j] = l[i]
        for j in range(0, n, 2):
            (l[i], l[j]) = (l[j], a)
            if l[j - 1] > a < l[j + 1] and eval(check):
                res += 2
            l[j] = l[i]
        for j in range(1, n, 2):
            (l[i], l[j]) = (l[j], a)
            if l[j - 1] < a > l[j + 1] and eval(check):
                res += 2
            l[j] = l[i]
        l[i] = a
    print(res // 2)


def __starting_point():
    main()


__starting_point()
